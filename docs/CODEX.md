# CODEX Instructions — Northstack

You are working inside the Northstack repository.

Before generating or modifying code, always read and follow:

- README.md
- docs/CONTEXT.md
- docs/ARCHITECTURE.md
- docs/AGENTS.md
- docs/ROADMAP.md

## Project Goal

Northstack is an agentic backend platform that transforms raw software project ideas into technical architecture blueprints.

## Package Management

This project uses `uv`.

Do NOT use:
- pip
- requirements.txt
- poetry

Always use:
- uv add
- uv sync
- uv run

## Core Stack

- Python
- FastAPI
- Agno
- OpenAI API
- Docker
- Docker Compose
- PostgreSQL

## Development Rules

Always:
- use type hints
- use Pydantic schemas
- keep FastAPI routes thin
- move business logic to services
- keep agent logic inside `app/agents`
- keep prompts inside `app/prompts`
- keep configuration inside `app/core`
- avoid hardcoded secrets
- use environment variables
- prefer simple, maintainable code

Avoid:
- unnecessary abstractions
- premature microservices
- complex multi-agent orchestration in the MVP
- Kubernetes
- frontend implementation for now
- authentication for now

## Current MVP

Build a FastAPI backend that exposes an endpoint to receive a project idea and return:

- project summary
- recommended stack
- architecture overview
- Mermaid diagram
- cloud suggestions
- MVP roadmap
- risks
- future evolution

## Suggested First Implementation

Create:

```txt
app/
├── main.py
├── api/
│   └── routes.py
├── schemas/
│   └── architecture.py
├── services/
│   └── architecture_service.py
├── agents/
│   └── architecture_agent.py
├── core/
│   └── config.py
└── prompts/
    └── architecture_prompt.py
