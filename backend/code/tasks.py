import os 
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code.settings')

import django

django.setup()

from code_test.end_meetings import auto_end_meeting

app = Celery('task', backend='rpc://', broker='pyamqp://')

app.conf.beat_schedule = {
    'end-meeting-everyday-midnight': {
        'task': 'tasks.end_meeting',
        'schedule': crontab(minute=0, hour=0),
    },
}

@app.task
def end_meeting():
    auto_end_meeting()