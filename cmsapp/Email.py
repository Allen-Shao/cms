from django.core.mail import send_mail


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