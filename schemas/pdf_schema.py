from pydantic import BaseModel
from datetime import datetime

class PdfBody(BaseModel):
    path: str


class PdfResponse(BaseModel):
    url: str
    status: bool
    data: datetime = datetime.now()