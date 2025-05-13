from pydantic import BaseModel
from typing import Any


class CheckRequest(BaseModel):
    user_task: str
    user_solution: str


class CheckResponse(BaseModel):
    result: Any  # можешь заменить на строгую структуру, если знаешь schema
