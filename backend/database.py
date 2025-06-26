import os
import databases
import sqlalchemy

# Загружаем DATABASE_URL из переменной окружения или .env
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/events_db")

# База данных и движок
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)

