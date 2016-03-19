from django.core.mail import send_mail

def sendToPublic(subject, message):
	send_mail('Subject', 'Here is the message.', 'nikv96@gmail.com',
    		['nikv96@gmail.com'], fail_silently=False)