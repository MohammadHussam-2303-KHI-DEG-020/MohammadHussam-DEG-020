from typing import List

def send_notification(user: dict) -> None:
    pass

def is_subscribed(user: dict) -> bool:
    return user.get('sub', False)

def notify_users(users: List[dict]) -> None:
    subscribed_users = filter(is_subscribed, users)
    for user in subscribed_users:
        send_notification(user)
