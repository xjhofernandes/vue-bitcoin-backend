from pydantic import BaseModel
from datetime import datetime

class RequestBody(BaseModel):
    period: str = None
    date_start: datetime = None
    date_end: datetime = None