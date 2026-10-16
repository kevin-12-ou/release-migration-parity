# Release Migration Parity

[简体中文](README.zh-CN.md) | [Skill instructions](SKILL.md) | [Maintainer: kevin-12-ou](https://github.com/kevin-12-ou)

**An AI agent skill for preserving accepted UI, behavior, and data semantics when releasing an app or migrating it to another platform.**

A build can pass while dialogs lose styles, two app modes stop sharing data, or a platform migration silently drops accepted behavior.

This is an **Agent Skill: instructions and reference material for an AI assistant**, not a hosted service or an autonomous program. The package contains no installation hooks, application runtime, models, background services, or credentials; its Python script is only for development-time package validation. The assistant still operates under its host permissions and the user's authorization.

## When to use it

- Use the accepted source and its actual working state as the baseline.
- Inspect routing, CSS scope, portals, identity, storage, and platform boundaries.
- Verify an end-to-end path before expanding a cross-platform migration.
- Tie the tested source, build artifact, deployment, and rollback together.

## Install

Use Git and an assistant that supports Agent Skills. The optional Skills CLI below also requires Node.js/npm and is a separate executable tool to review before running. This skill itself needs no API key, database, or paid account; your chosen AI assistant may have its own costs.

```sh
npx skills add kevin-12-ou/release-migration-parity --skill release-migration-parity
```

Choose the agent and scope in the installer. For a project-local Codex installation, with copied files rather than symlinks:

```sh
npx skills add kevin-12-ou/release-migration-parity --skill release-migration-parity --agent codex --copy
```

Manual option: copy the complete repository into a skill directory named `release-migration-parity`, such as `.agents/skills/release-migration-parity/`, where supported by your assistant. Keep `SKILL.md` and its referenced files together; follow your client's skill-directory documentation.

## Example prompts

```text
Use $release-migration-parity. Publish the accepted experimental version while preserving its dialogs, theme, data semantics, and existing entry points. Verify the actual deployed flow and provide a rollback reference.
```

```text
用 $release-migration-parity。把已验收实验版上线，保留弹窗、主题、数据语义和既有入口。验证实际线上流程，并说明回退位置。
```

```text
Use $release-migration-parity. Port this working web app to a WeChat Mini Program. Preserve the web version, compare platform constraints, and verify one edit-save-reopen path before expanding.
```

```text
用 $release-migration-parity。把这个可用网页迁到微信小程序，保留网页原版，核对平台差异，先验证一条编辑、保存、重开的完整路径。
```

Explicitly naming the skill helps make intent clear. Automatic selection depends on the model and client and is not guaranteed. The package follows the [Agent Skills specification](https://agentskills.io/specification); clients such as Codex and Claude Code can read this format, but equivalent behavior across every client is not claimed. Core instructions are primarily Chinese; this English README provides discovery and usage context.

## Boundaries and data

Not a promise of zero bugs or identical source code across platforms. Compilation, HTTP availability, browser interaction, and real-device behavior are distinct evidence levels.

No private project history is bundled. File access, network requests, commands, and edits depend on the task and the assistant's tools. A text skill is not an isolation boundary or a mandatory security interceptor.

## Maintenance and feedback

For Skills CLI installs, `npx skills check` checks for updates and `npx skills update` updates installed skills. Review changes first. Disable the skill in your client, or move its installed directory out of discovery, to stop using it. Back up any personal additions before updating or removing it.

Report a sanitized example in [Issues](https://github.com/kevin-12-ou/release-migration-parity/issues). See [CONTRIBUTING.md](CONTRIBUTING.md) and [VALIDATION.md](VALIDATION.md) for contribution and validation boundaries.

## Related skills by kevin-12-ou

- [Concept to Action Coach](https://github.com/kevin-12-ou/concept-to-action-coach) — An AI agent skill for explaining technical concepts to beginners and turning understanding into a small, verifiable action.
- [Don't Repeat Yourself](https://github.com/kevin-12-ou/dont-repeat-yourself) — An AI agent skill for saving verified coding solutions as searchable recipes and adapting them to future projects.
- [Deploy Onboarding Guide](https://github.com/kevin-12-ou/deploy-onboarding-guide) — A Chinese-first AI agent skill for assessing open-source software before installation and explaining setup, permissions, costs, and first use.

Maintained by [kevin-12-ou](https://github.com/kevin-12-ou). Developed from personal AI-assisted workflows. Licensed under [MIT](LICENSE); see [NOTICE.md](NOTICE.md) for provenance.
