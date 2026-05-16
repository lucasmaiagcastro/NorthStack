from agno.agent import Agent
from agno.models.openai import OpenAIChat

from app.prompts.architecture_prompt import ARCHITECTURE_AGENT_INSTRUCTIONS
from app.schemas.architecture import ArchitecturePlanRequest, ArchitecturePlanResponse


class ArchitectureAgent:
    def __init__(self, api_key: str, model_id: str) -> None:
        self._agent = Agent(
            name="Architecture Agent",
            model=OpenAIChat(
                api_key=api_key,
                id=model_id,
            ),
            instructions=ARCHITECTURE_AGENT_INSTRUCTIONS,
            output_schema=ArchitecturePlanResponse,
            parse_response=True,
        )

    def generate_plan(
        self,
        request: ArchitecturePlanRequest,
    ) -> ArchitecturePlanResponse:
        response = self._agent.run(
            request.model_dump_json(exclude_none=True),
        )

        if isinstance(response.content, ArchitecturePlanResponse):
            return response.content

        if isinstance(response.content, dict):
            return ArchitecturePlanResponse.model_validate(response.content)

        if isinstance(response.content, str):
            return ArchitecturePlanResponse.model_validate_json(response.content)

        return ArchitecturePlanResponse.model_validate(response.content)
