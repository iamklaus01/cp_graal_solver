from pydantic import BaseModel


class ProblemIn(BaseModel):
    content: str
    user_id: int


class Problem(BaseModel):
    id: int
    content: float
    user_id: int
