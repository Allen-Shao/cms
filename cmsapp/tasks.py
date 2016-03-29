from __future__ import absolute_import
from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import group
from datetime import timedelta
from Email import send_to_president


logger = get_task_logger(__name__)


@task(name="pmo-emailer", bind=True)
def email_pmo(self):
    """
        Send PMO Email every half hour
    """
    send_to_president()
    return 'Success'