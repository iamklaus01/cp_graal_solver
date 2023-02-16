from typing import List
from pydantic import BaseModel

from db.tables import Metric, Operator


class ConstraintIn(BaseModel):
    coefficient: List[int]
    operators: List[Operator]
    metric: Metric
    value: float
    variable_id: int


class Constraint(BaseModel):
    id: int
    coefficient: List[int]
    operators: List[Operator]
    metric: Metric
    value: float
    variable_id: int
