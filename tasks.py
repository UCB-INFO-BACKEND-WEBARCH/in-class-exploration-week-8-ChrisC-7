from rq.decorators import job 
from redis import Redis
import time
import os

redis_conn = Redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))

@job('notifications', connection=redis_conn)
def send_notification(notification_id, email, message):
    print(f'Sending to {email}...')
    time.sleep(3)
    print(f"Sent: {message}")
    return {"notification_id": notification_id,
            "email":email,
            "status": "sent",
            "sent_at":time.ctime()}
