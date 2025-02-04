import vk_api
from vk_api.longpoll import VkLongPoll
from app.config import VK_GROUP_TOKEN, VK_GROUP_ID
from app.database import init_db, SessionLocal
from app.handlers import handle_event
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def main():
    if not VK_GROUP_TOKEN or not VK_GROUP_ID:
        raise ValueError("Укажите VK_GROUP_TOKEN и VK_GROUP_ID в файле .env")

    # инициализация базы данных (с ожиданием готовности)
    init_db()
    db_session = SessionLocal()

    # инициализация vk_api
    vk_session = vk_api.VkApi(token=VK_GROUP_TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    print("Бот запущен. Ожидание событий...")

    for event in longpoll.listen():
        handle_event(event, vk_session, vk, db_session)

if __name__ == '__main__':
    main()
