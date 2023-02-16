from typing import List
from pydantic import BaseModel

from db.tables import VariableType, DomainType


class VariableIn(BaseModel):
    name: str
    type: VariableType
    domain_type: DomainType
    domain_value: List[float]
    problem_id: int


class Variable(BaseModel):
    id: int
    name: str
    type: VariableType
    domain_type: DomainType
    domain_value: List[float]
    problem_id: int