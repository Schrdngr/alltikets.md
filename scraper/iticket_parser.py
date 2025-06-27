import httpx
from bs4 import BeautifulSoup
from backend.database import database
from backend.models import events
import uuid

BASE_URL = "https://iticket.md"

async def run():
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
        soup = BeautifulSoup(response.text, "html.parser")

        event_blocks = soup.select(".event")[:10] # берём 10 первых событий
        for block in event_blocks:
            try:
                title = block.select_one(".event-title").text.strip()
                url = BASE_URL + block.select_one("a")["href"]
                image = block.select_one("img")["src"]
                date = block.select_one(".event-date").text.strip()
                location = block.select_one(".event-location").text.strip()

                # Пока цена не указывается, просто пустая строка
                price = ""

                query = events.insert().values(
                    title=title,
                    description="",
                    date=date,
                    location=location,
                    price=price,
                    url=url,
                    image_url=image,
                    source="iticket.md"
                )
                await database.execute(query)
            except Exception as e:
                print(f"Ошибка при парсинге блока: {e}")

