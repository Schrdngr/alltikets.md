import sqlalchemy
from backend.database import metadata

events = sqlalchemy.Table(
    "events",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("date", sqlalchemy.String), # Можно заменить на DateTime
    sqlalchemy.Column("location", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.String),
    sqlalchemy.Column("url", sqlalchemy.String),
    sqlalchemy.Column("image_url", sqlalchemy.String),
    sqlalchemy.Column("source", sqlalchemy.String), # iticket.md, mticket.md и т.д.
)

