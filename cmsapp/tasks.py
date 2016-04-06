from __future__ import absolute_import
from celery.decorators import task, periodic_task
from celery import group
from datetime import timedelta
from . import Email
from celery.task.schedules import crontab

@periodic_task(run_every=(crontab(minute='*/1')), name="pmo_emailer", ignore_result=True)
def email_pmo():
    """
        Send PMO Email every half hour
    """
    Email.send_email()
    return 'Success'