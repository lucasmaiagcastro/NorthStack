from app.agents.architecture_agent import ArchitectureAgent
from app.core.config import settings
from app.schemas.architecture import (
    ArchitecturePlanRequest,
    ArchitecturePlanResponse,
    RecommendedStack,
)


def _mock_architecture_plan(
    request: ArchitecturePlanRequest,
) -> ArchitecturePlanResponse:
    return ArchitecturePlanResponse(
        project_summary=f"Architecture plan for: {request.project_idea}",
        recommended_stack=RecommendedStack(
            backend="FastAPI",
            database="PostgreSQL",
            cache="Redis",
            cloud=request.constraints.cloud if request.constraints else "aws",
            containerization="Docker",
        ),
        architecture_overview=(
            "Start with a modular monolith architecture. Keep the system simple, "
            "containerized and easy to evolve before introducing distributed services."
        ),
        mermaid_diagram="""
flowchart TD
    USER[User]
    API[FastAPI Backend]
    DB[(PostgreSQL)]
    CACHE[(Redis)]

    USER --> API
    API --> DB
    API --> CACHE
""".strip(),
        mvp_scope=[
            "Create FastAPI backend",
            "Add PostgreSQL persistence",
            "Containerize with Docker",
            "Generate architecture reports",
        ],
        risks=[
            "Overengineering too early",
            "Choosing cloud services before validating the MVP",
            "Lack of clear non-functional requirements",
        ],
        future_evolution=[
            "Add async workers",
            "Add cloud deployment",
            "Add architecture comparison mode",
        ],
    )


def generate_architecture_plan(
    request: ArchitecturePlanRequest,
) -> ArchitecturePlanResponse:
    if not settings.openai_api_key:
        return _mock_architecture_plan(request)

    try:
        agent = ArchitectureAgent(
            api_key=settings.openai_api_key,
            model_id=settings.openai_model,
        )
        return agent.generate_plan(request)
    except Exception:
        return _mock_architecture_plan(request)
