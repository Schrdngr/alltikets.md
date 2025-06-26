from pydantic import BaseModel

class Event(BaseModel):
    id: int
    title: str
    description: str | None = None
    date: str | None = None
    location: str | None = None
    price: str | None = None
    url: str | None = None
    image_url: str | None = None
    source: str | None = None

    class Config:
        orm_mode = True

