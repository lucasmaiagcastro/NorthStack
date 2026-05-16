from app.schemas.architecture import (
    ArchitectureConstraints,
    ArchitecturePlanRequest,
    ArchitecturePlanResponse,
)
from app.services import architecture_service


def test_generate_architecture_plan_uses_mock_fallback_without_api_key(
    monkeypatch,
) -> None:
    request = ArchitecturePlanRequest(
        project_idea="Build a SaaS platform for price monitoring.",
        constraints=ArchitectureConstraints(cloud="aws"),
    )

    monkeypatch.setattr(architecture_service.settings, "openai_api_key", None)

    response = architecture_service.generate_architecture_plan(request)

    assert response.project_summary == (
        "Architecture plan for: Build a SaaS platform for price monitoring."
    )
    assert response.recommended_stack.backend == "FastAPI"
    assert response.recommended_stack.database == "PostgreSQL"
    assert response.recommended_stack.cloud == "aws"


def test_generate_architecture_plan_returns_architecture_plan_response(
    monkeypatch,
) -> None:
    request = ArchitecturePlanRequest(
        project_idea="Build an internal tool for engineering planning.",
    )

    monkeypatch.setattr(architecture_service.settings, "openai_api_key", None)

    response = architecture_service.generate_architecture_plan(request)

    assert isinstance(response, ArchitecturePlanResponse)
