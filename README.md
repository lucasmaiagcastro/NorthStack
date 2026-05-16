# Northstack

Northstack is a FastAPI backend that turns raw software project ideas into
structured technical architecture plans.

The current MVP receives a project idea, sends it through an architecture
planning service, and returns a typed JSON response with stack recommendations,
architecture overview, Mermaid diagram, MVP scope, risks, and future evolution
notes.

Northstack is intended to behave like a practical software architecture
assistant, focused on maintainable systems and realistic engineering tradeoffs.

---

## Current Status

Current stage: MVP architecture planning backend.

Implemented:

- FastAPI application
- Health check endpoint
- Architecture planning endpoint
- Pydantic request and response schemas
- Architecture service layer
- Agno/OpenAI-backed architecture agent
- Mock fallback when `OPENAI_API_KEY` is not configured
- Minimal pytest coverage for the architecture service

Not implemented yet:

- Frontend
- Authentication
- Database persistence
- Report storage
- Multi-agent orchestration
- Cloud cost estimation
- Production deployment setup

---

## Tech Stack

- Python 3.14+
- FastAPI
- Pydantic
- Agno
- OpenAI API
- uv
- pytest
- Ruff

Planned later:

- PostgreSQL
- Docker / Docker Compose
- Redis
- pgvector
- AWS integrations
- Observability
- RAG

---

## Setup

Install dependencies:

```bash
uv sync
```

Run the API locally:

```bash
uv run uvicorn app.main:app --reload
```

Open the interactive API docs:

```txt
http://127.0.0.1:8000/docs
```

---

## Configuration

Northstack reads configuration from environment variables and, in local
development, from `.env`.

Supported settings:

```env
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
APP_ENV=development
```

If `OPENAI_API_KEY` is not set, the architecture service returns a deterministic
mock architecture plan. This keeps local development and tests independent from
the real OpenAI API.

Do not commit secrets.

---

## API

### `GET /`

Basic root endpoint.

Example response:

```json
{
  "message": "Northstack is running"
}
```

### `GET /health`

Health check endpoint.

Example response:

```json
{
  "status": "ok"
}
```

### `POST /architecture/plan`

Generates a structured architecture plan from a project idea.

Example request:

```json
{
  "project_idea": "I want to build a SaaS platform for price monitoring with alerts and dashboards.",
  "constraints": {
    "budget": "low",
    "cloud": "aws",
    "team_size": "solo developer",
    "experience_level": "intermediate"
  }
}
```

Example response shape:

```json
{
  "project_summary": "Architecture plan for: I want to build a SaaS platform for price monitoring with alerts and dashboards.",
  "recommended_stack": {
    "backend": "FastAPI",
    "database": "PostgreSQL",
    "cache": "Redis",
    "cloud": "aws",
    "containerization": "Docker"
  },
  "architecture_overview": "Start with a modular monolith architecture...",
  "mermaid_diagram": "flowchart TD\n    USER[User]\n    API[FastAPI Backend]",
  "mvp_scope": [
    "Create FastAPI backend",
    "Add PostgreSQL persistence"
  ],
  "risks": [
    "Overengineering too early"
  ],
  "future_evolution": [
    "Add async workers"
  ]
}
```

---

## Development

Run tests:

```bash
uv run pytest
```

Run tests for the architecture service only:

```bash
uv run pytest tests/services/test_architecture_service.py
```

Run lint checks:

```bash
uv run ruff check app tests
```

---

## Project Structure

```txt
app/
├── agents/
│   └── architecture_agent.py
├── api/
│   └── routes.py
├── core/
│   └── config.py
├── prompts/
│   └── architecture_prompt.py
├── schemas/
│   └── architecture.py
├── services/
│   └── architecture_service.py
└── main.py

docs/
├── AGENTS.md
├── ARCHITECTURE.md
├── CODEX.md
├── CONTEXT.md
└── ROADMAP.md

tests/
└── services/
    └── test_architecture_service.py
```

---

## Design Principles

Northstack favors:

- simple architecture first
- typed schemas
- thin API routes
- business logic in services
- agent logic isolated in `app/agents`
- prompts isolated in `app/prompts`
- practical recommendations over buzzwords
- incremental evolution instead of premature complexity

Northstack avoids:

- frontend work during the current MVP
- database persistence until explicitly added
- unnecessary multi-agent orchestration
- hardcoded secrets
- overengineered abstractions

---

## Documentation

Project documentation lives in `docs/`:

- `docs/CONTEXT.md`
- `docs/ARCHITECTURE.md`
- `docs/AGENTS.md`
- `docs/ROADMAP.md`
- `docs/CODEX.md`

---

## License

MIT
