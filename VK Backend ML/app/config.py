import os
from dotenv import load_dotenv

load_dotenv()  # загружаем переменные окружения из файла .env

VK_GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN")
VK_GROUP_ID = os.getenv("VK_GROUP_ID")
DATABASE_URL = os.getenv("DATABASE_URL")
RESET_DB = os.getenv("RESET_DB", "false").lower() == "true"
