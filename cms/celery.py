from __future__ import absolute_import
import os
from celery import Celery
from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')

from django.conf import settings

settings.configure()

BROKER_URL = 'redis://localhost:6379'

cmscelery = Celery('cmsapp',
					broker='redis://',
             		backend='redis://',
             		include=['cmsapp.tasks'])

# Using a string here means the worker will not have to
# pickle the object when using Windows.
cmscelery.config_from_object('django.conf:settings')
cmscelery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


CELERYBEAT_SCHEDULE = {
    'send-pmo-email-every-halfhour': {
        'task': 'tasks.email_pmo',
        'schedule': timedelta(seconds=30),
        'args': ()
    },
}

if __name__ == '__main__':
    cmscelery.start()