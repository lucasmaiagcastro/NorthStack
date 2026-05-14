from pydantic import BaseModel, Field


class ArchitectureConstraints(BaseModel):
    budget: str | None = Field(default=None, examples=["low"])
    cloud: str | None = Field(default=None, examples=["aws"])
    team_size: str | None = Field(default=None, examples=["solo developer"])
    experience_level: str | None = Field(default=None, examples=["junior/intermediate"])


class ArchitecturePlanRequest(BaseModel):
    project_idea: str = Field(..., min_length=10)
    constraints: ArchitectureConstraints | None = None


class RecommendedStack(BaseModel):
    backend: str
    database: str
    cache: str | None = None
    cloud: str | None = None
    containerization: str


class ArchitecturePlanResponse(BaseModel):
    project_summary: str
    recommended_stack: RecommendedStack
    architecture_overview: str
    mermaid_diagram: str
    mvp_scope: list[str]
    risks: list[str]
    future_evolution: list[str]
