from django.core.mail import send_mail
from models import Decision

def send_email():
    flag = True
    for decision in Decision.objects.all():
      if decision.active == True:
        message = "Dear Sir,\n\nThe following crisis has occured: " + \
                    decision.type_of_crisis.__unicode__() + "\n\nThe details are as follows: " +  \
              decision.description + "\n\nDate and Time: " + str(decision.date_time) \
              + "Best,\nAllStarCMS"
        send_to_president(message)
        flag = False
#    if flag:
#      send_to_president()

def send_to_president():
    """
    Send periodic messages to the PMO when all is well!

    :return: None
    """
    send_mail("Periodic Report"
              , "Dear Sir,\n\nThe situation is fine.\n\nBest,\nAllStarCMS"
              , 'allstarscms3003@gmail.com',
              ['nikv96@gmail.com'], fail_silently=False)


def send_to_president(message):
    """
    Send custom message to PMO in case of any issue

    :param message: Custom message to be sent to the PMO
    :return: None
    """
    send_mail("Periodic Report"
              , message
              , 'allstarscms3003@gmail.com',
              ['nikv96@gmail.com'],
              #['weifengzi2009@gmail.com'],
              fail_silently=False)
