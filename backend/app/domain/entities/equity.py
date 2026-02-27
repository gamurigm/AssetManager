from pydantic import BaseModel

class EquityCurvePoint(BaseModel):
    time: int
    realized: float
    total: float
