from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import models, database, crud, schemas

app = FastAPI(
    title="Event Aggregator API",
    description="Агрегация билетов с iticket.md, mticket.md, afisha.md и др.",
    version="1.0.0"
)

# Разрешаем CORS для фронтенда (замени на свой домен при деплое)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # В проде лучше указать конкретный фронт
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация БД
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Роут: получить список событий
@app.get("/events", response_model=list[schemas.Event])
async def get_all_events():
    return await crud.get_all_events()
