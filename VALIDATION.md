# Validation and evidence

## Automated package checks

Run with Python 3.10+:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

The pinned development dependency is PyYAML 6.0.3. It is not required for the assistant to read or use this skill.

The validator checks required files, YAML metadata and UI prompt consistency, Markdown links to local resources, selected accidental credential/path patterns, and the empty public recipe library where applicable. GitHub Actions runs the same check on pushes and pull requests with read-only repository permissions.

## What this does not establish

Format and packaging checks do not prove reliable automatic invocation, improved model quality, complete security, correct behavior in every client, or a successful production deployment. Installing the package proves file discovery and delivery, not the quality of a future response.

The core instructions come from an existing personal workflow. The public package adds metadata and documentation; its migration example has been generalized to remove private project history. Keep observed runtime behavior separate from the intended workflow described in the README.

For behavior changes, provide a realistic prompt and compare the result before and after the change. Record the agent/model, environment, observed actions, and unverified portions. For release or migration use, real application and device checks still belong to that specific project.
