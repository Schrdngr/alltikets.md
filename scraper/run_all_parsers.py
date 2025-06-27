import asyncio
from scraper import iticket_parser, mticket_parser, afisha_parser, livetickets_parser

async def main():
    print("🔄 Запуск всех парсеров...")
    
    await iticket_parser.run()
    print("✅ iticket_parser завершён")

    await mticket_parser.run()
    print("✅ mticket_parser завершён")

    await afisha_parser.run()
    print("✅ afisha_parser завершён")

    await livetickets_parser.run()
    print("✅ livetickets_parser завершён")

    print("🎉 Все парсеры завершены")

if __name__ == "__main__":
    asyncio.run(main())

