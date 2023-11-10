import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers import user_handlers
from dotenv import load_dotenv

load_dotenv()
# Теперь переменная BOT_TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения

token = os.getenv('BOT_TOKEN',
                  default='6659854208:AAGvQY2TZF1E1Tm-xz8X0vC348HvXYTu80w')


# Функция конфигурирования и запуска бота
async def main():

    # Инициализируем бот и диспетчер
    bot = Bot(token=token)
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    # dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
