from pydantic import BaseModel

class Resource(BaseModel):
    url: str
    alt_text: str | None = None
