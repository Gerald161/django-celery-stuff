import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookingProject.settings')

app = Celery('bookingProject')

app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# Celery Beat Settings
# app.conf.beat_schedule = {
#     'test-at-1': {
#         'task': 'account.tasks.add',
#         # 'schedule': crontab(hour=13, minute=2, day_of_month=14, month_of_year = 4),
#         # day_of_week parameter optional
#         'schedule': crontab(hour=13, minute=55),
#         'args': (2,4)
#     },
#     # 'run-every-1-minute': {
#     #     'task': 'account.tasks.subs',
#     #     'schedule': timedelta(minutes=1),
#     #     "args": ("2")
#     # },
# }