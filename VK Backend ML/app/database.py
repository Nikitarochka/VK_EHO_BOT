import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL, RESET_DB
from app.models import Base

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def wait_for_db(timeout=60):
    """Ожидаем готовность базы данных в течение timeout секунд."""
    start = time.time()
    while True:
        try:
            conn = engine.raw_connection()
            conn.close()
            print("База данных готова для соединения!")
            break
        except OperationalError:
            if time.time() - start > timeout:
                raise Exception(f"База данных не готова после {timeout} секунд")
            print("Ожидание базы данных...")
            time.sleep(1)

def init_db():
    wait_for_db(timeout=60)
    if RESET_DB:
        print("RESET_DB=true: Очистка базы данных...")
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
