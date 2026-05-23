# Claude Code Instructions — Northstack

Always communicate with me in Brazilian Portuguese.

Code, comments, docstrings, commit messages and technical identifiers should remain in English unless I explicitly ask otherwise.

Before modifying code, read:
- README.md
- docs/CONTEXT.md
- docs/ARCHITECTURE.md
- docs/CODEX.md
- docs/AGENTS.md
- docs/ROADMAP.md

Project stack:
- Python
- uv
- FastAPI
- Agno
- OpenAI API
- PostgreSQL later
- Docker later

Rules:
- Use uv only. Do not use pip, poetry or requirements.txt.
- Do not run git commands.
- Do not modify .env.
- Do not expose secrets.
- Keep the project modular and simple.
- Avoid overengineering.
- Prefer FastAPI, Python, PostgreSQL, Docker and Agno.
- Do not add frontend, database persistence or multi-agent orchestration unless requested.

Before modifying files:
1. Explain the implementation plan.
2. List all files that will change.
3. Explain exactly what will be added or removed.
4. Wait for my approval.

Safe commands:
- uv run pytest
- uv run ruff check app tests
- uv run python -c "..."
- ls
- cat
- grep

Ask before:
- deleting files
- changing dependencies
- Docker commands
- network calls
- git commands
- modifying .env
