# Northstack

Northstack is an agentic backend platform that transforms raw software ideas into structured technical architecture blueprints.

The platform uses AI agents to analyze project requirements and generate:

- recommended stacks
- architecture decisions
- cloud suggestions
- scalability considerations
- Mermaid diagrams
- implementation roadmaps
- MVP recommendations
- technical risks

The goal is to help developers and teams design software architectures before writing code.

---

# Vision

Many developers can generate code using AI tools, but still struggle with:

- software architecture
- infrastructure decisions
- scalability planning
- backend structuring
- cloud design
- engineering tradeoffs

Northstack aims to become an intelligent architecture copilot focused on practical and maintainable engineering decisions.

---

# Setup

## Install dependencies

```bash
uv sync
```

## Run locally

```bash
uv run uvicorn app.main:app --reload
```

---

# Tech Stack

## Backend
- Python
- FastAPI
- Agno

## AI
- OpenAI API

## Infrastructure
- Docker
- Docker Compose
- OrbStack

## Database
- PostgreSQL

## Future Additions
- Redis
- pgvector
- AWS integrations
- Observability
- RAG
- Streaming responses

---

# Core Features

- Project architecture planning
- Stack recommendations
- Cloud service suggestions
- Mermaid diagram generation
- MVP scoping
- Technical roadmap generation
- Engineering tradeoff analysis

---

# Example Input

```json
{
  "project_idea": "I want to build a SaaS platform for price monitoring with alerts and dashboards.",
  "constraints": {
    "budget": "low",
    "cloud": "aws",
    "team_size": "solo developer"
  }
}
```

# Example Output

- Recommended backend stack
- Database choice
- Cloud architecture
- Mermaid diagrams
- MVP roadmap
- Risks and tradeoffs
- Scaling suggestions

---

# Project Philosophy

Northstack avoids overengineering.

The system should prioritize:
- simplicity
- maintainability
- cost efficiency
- realistic architectures
- practical engineering decisions

This is not a "generate random enterprise architecture" tool.

The focus is:
- useful architectures
- solo developer friendly systems
- startup-friendly infrastructure
- scalable evolution paths

---

# Development Status

Current stage:
- MVP architecture planning

Planned:
- multi-agent orchestration
- architecture memory
- cloud cost estimation
- frontend dashboard
- architecture comparison mode

---

## Documentation

Project documentation is available inside the `/docs` folder.

- Architecture
- Agents
- Roadmap
- AI assistant context
- Engineering decisions

---

# Local Development

## Run with Docker

```bash
docker compose up --build
```

## Run locally

```bash
uvicorn app.main:app --reload
```

---

# License

MIT
