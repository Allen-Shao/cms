from django.core.mail import send_mail


def send_to_president():
    """
    Send periodic messages to the PMO when all is well!

    :return: None
    """
    send_mail("Periodic Report"
              , "Everything is fine boss."
              , 'allstarscms3003@gmail.com',
              ['nikv96@gmail.com'], fail_silently=False)


def send_to_pres(message):
    """
    Send custom message to PMO in case of any issue

    :param message: Custom message to be sent to the PMO
    :return: None
    """
    send_mail("Periodic Report"
              , message
              , 'allstarscms3003@gmail.com',
              # ['nikv96@gmail.com'],
              ['weifengzi2009@gmail.com'],
              fail_silently=False)


def send_to_agency(message):
    """
    Send email to specific entities with a specific message

    :param message: Custom message to be sent to the entities
    :return: None
    """
    send_mail("NOTIFICATION"
              , message
              , 'allstarscms3003@gmail.com',
              to, fail_silently=False)
