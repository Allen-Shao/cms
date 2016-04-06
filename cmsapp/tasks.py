from __future__ import absolute_import
from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import group
from datetime import timedelta
from . import Email

logger = get_task_logger(__name__)


@task(name="pmo-emailer", bind=True)
def email_pmo(self):
    """
        Send PMO Email every half hour
    """
    Email.send_email()
    return 'Success'