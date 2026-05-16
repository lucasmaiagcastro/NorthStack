# Codex Project Instructions — Northstack

Always communicate with me in Brazilian Portuguese.

Code, comments, docstrings, commit messages and technical identifiers should remain in English unless I explicitly ask otherwise.

Before modifying code, read:
- README.md
- docs/CONTEXT.md
- docs/ARCHITECTURE.md
- docs/CODEX.md
- docs/AGENTS.md
- docs/ROADMAP.md

Project rules:
- Use uv only. Do not use pip, poetry or requirements.txt.
- Do not run git commands.
- Do not modify .env.
- Do not expose secrets.
- Keep the project modular and simple.
- Avoid overengineering.
- Prefer FastAPI, Python, PostgreSQL, Docker and Agno.
- Do not add frontend, database persistence or multi-agent orchestration unless requested.

When running commands:
- You may run safe read/check commands such as:
  - uv run ruff check app
  - uv run pytest
  - uv run python -c "..."
  - ls
  - cat
  - grep
- Ask before destructive commands, dependency changes, Docker commands, network calls, file deletion or anything involving Git.
