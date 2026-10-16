"""Validate this public skill package; no project code or skill commands are run."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

import yaml


def validate(root):
    errors = []
    required = ['SKILL.md', 'README.md', 'README.zh-CN.md', 'LICENSE',
                'NOTICE.md', 'CONTRIBUTING.md', 'SECURITY.md', 'VALIDATION.md',
                'agents/openai.yaml', 'llms.txt']
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f'Missing file: {relative}')
    if errors:
        return errors
    skill_path = root / 'SKILL.md'
    if not skill_path.is_file():
        return errors
    content = skill_path.read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---\n', content, re.S)
    if not match:
        errors.append('SKILL.md needs YAML frontmatter')
        return errors
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f'Invalid frontmatter: {exc}')
        return errors
    if not isinstance(meta, dict):
        return errors + ['Frontmatter must be a mapping']
    name = meta.get('name', '')
    if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        errors.append('Invalid skill name')
    if name != root.name:
        errors.append('Skill name must match its directory name')
    description = meta.get('description', '')
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        errors.append('Description must be a non-empty string of at most 1024 characters')
    if meta.get('license') != 'MIT':
        errors.append('Expected MIT license metadata')
    metadata = meta.get('metadata')
    if not isinstance(metadata, dict) or not all(isinstance(k,str) and isinstance(v,str) for k,v in metadata.items()):
        errors.append('metadata must map strings to strings')
    if 'MIT License' not in (root / 'LICENSE').read_text(encoding='utf-8'):
        errors.append('License file is inconsistent')
    ui_path = root / 'agents/openai.yaml'
    if ui_path.is_file():
        try:
            ui = yaml.safe_load(ui_path.read_text(encoding='utf-8'))['interface']
            if '$' + str(name) not in ui.get('default_prompt', ''):
                errors.append('UI default_prompt must name the skill')
            if not ui.get('display_name') or not 25 <= len(ui.get('short_description','')) <= 64:
                errors.append('UI title or short description is invalid')
        except (yaml.YAMLError, KeyError, TypeError):
            errors.append('Invalid agents/openai.yaml')

    patterns = {
        'machine-specific user path': r'\b[A-Za-z]:[\\/](?:Users|AI)[\\/]',
        'private key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
        'GitHub token': r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b',
        'API key': r'\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b',
    }
    files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts]
    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f'Unexpected symlink: {rel}')
            continue
        if path.name == '.env' or path.name.startswith('.env.') or path.suffix in {'.pem','.key'}:
            errors.append(f'Unexpected credential file: {rel}')
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            errors.append(f'Unexpected binary file: {rel}')
            continue
        for label, pattern in patterns.items():
            if re.search(pattern, text):
                errors.append(f'{label} pattern found in {rel}; inspect locally')
        if path.suffix != '.md':
            continue
        for link in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)', text):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
                continue
            relative = unquote(link.split('#',1)[0])
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f'Broken or escaping local link in {rel}: {link}')

    if name == 'dont-repeat-yourself':
        for folder in ['recipes','artifacts']:
            actual = [p for p in (root/'library'/folder).rglob('*') if p.is_file() and p.name != '.gitkeep']
            if actual:
                errors.append(f'Public package must not include private library/{folder} content')
        index = (root/'library/INDEX.md').read_text(encoding='utf-8')
        if len([line for line in index.splitlines() if line.startswith('|')]) != 2:
            errors.append('Public recipe index must contain headers only')
    return errors


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    for problem in problems:
        print('FAIL:', problem)
    if problems:
        sys.exit(1)
    print(f'PASS: {root.name}: metadata, UI, local links, public file set, selected disclosure checks')
