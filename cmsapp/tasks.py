from __future__ import absolute_import
from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import group
from datetime import timedelta
import Email
from models import Decision


logger = get_task_logger(__name__)


@task(name="pmo-emailer", bind=True)
def email_pmo(self):
    """
        Send PMO Email every half hour
    """
    flag = True
    for decision in Decision.objects.all():
    	if decision.active == True:
    		message = "Dear Sir,\n\nThe following crisis has occured: "+
    					decision.type_of_crisis + "\n\nThe details are as follows: "+
    					decision.description + "\n\nDate and Time: " + decision.date_time
    					+ "Best,\nAllStarCMS"
    		Email.send_to_president(message)
    		flag = False
    if flag:
    	Email.send_to_president()
    return 'Success'