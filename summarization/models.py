from fastapi_utils.api_model import APIModel


class SummarizationRequest(APIModel):
    paper_content: str
    preferred_model: str
    maximum_tokens: int
    model_task: str


class SummarizationResponse(APIModel):
    output: str


class AvailableModel:
    def __init__(self, hf_model_id: str, display_name: str, task: str):
        self.hf_model_id = hf_model_id
        self.display_name = display_name
        self.task = task

    def __hash__(self):
        return hash(self.hf_model_id)
