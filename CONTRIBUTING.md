# Contributing

Open an issue with the user goal, a sanitized prompt, relevant host/model details, expected result, actual result, and verification limits. Never include credentials, private chats, customer data, personal recipe libraries, or unredacted logs.

Keep the skill focused. Prefer a narrow correction supported by a reproducible scenario over adding universal rules. Preserve the user's scope, choices, and existing authorization. Update both README languages when public usage changes.

Before a pull request, run `python -m pip install -r requirements-dev.txt` and `python scripts/validate.py`. Behavioral changes also need a realistic before/after scenario; format validation alone does not prove improved agent behavior.
