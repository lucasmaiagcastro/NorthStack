from fastapi import APIRouter

from app.schemas.architecture import ArchitecturePlanRequest, ArchitecturePlanResponse
from app.services.architecture_service import generate_architecture_plan

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Northstack is running"}


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/architecture/plan", response_model=ArchitecturePlanResponse)
async def create_architecture_plan(
    request: ArchitecturePlanRequest,
) -> ArchitecturePlanResponse:
    return generate_architecture_plan(request)
