from __future__ import absolute_import,unicode_literals
from celery import Celery


app=Celery('bank')

app.config_from_object('config.py')

app.autodiscover_tasks('tasks.py')