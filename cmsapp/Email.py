from django.core.mail import send_mail

def sendToPublic(subject, message, to):
	send_mail("Periodic Report"
		, "Everything is fine boss."
		, 'allstarscms3003@gmail.com', 
		['nikv96@gmail.com'], fail_silently=False)