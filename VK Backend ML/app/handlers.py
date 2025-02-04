import logging
import random
from app.models import User

logger = logging.getLogger(__name__)

def handle_event(event, vk_session, vk_api, db_session):
    # обрабатываем только личные сообщения, адресованные боту (тип 4)
    if event.type != 4 or not event.to_me:
        return

    user_id = event.user_id
    logger.info(f"Получено сообщение от {user_id}")

    # приветственное сообщение для нового пользователя
    user = db_session.query(User).filter(User.user_id == user_id).first()
    if user is None:
        try:
            vk_api.messages.send(
                peer_id=user_id,
                message="Привет! Добро пожаловать.",
                random_id=random.randint(1, 10**6)
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке приветственного сообщения: {e}")
        new_user = User(user_id=user_id, greeted=True)
        db_session.add(new_user)
        db_session.commit()

    # если в сообщении есть вложения, пересылаем исходное сообщение обратно
    attachments = getattr(event, "attachments", None)
    if attachments is None and hasattr(event, "object"):
        attachments = event.object.get("attachments", {})

    if attachments:
        try:
            vk_api.messages.send(
                peer_id=user_id,
                message=".",  # непустой текст (пустой выдаёт ошибку, пробел тоже)
                forward_messages=str(event.message_id),
                random_id=random.randint(1, 10**6)
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке пересланного сообщения: {e}")
    else:
        logger.info("Вложений не обнаружено, отправляем только приветствие.")
