from django.core.mail import send_mail

def send_to_president():
	send_mail("Periodic Report"
		, "Everything is fine boss."
		, 'allstarscms3003@gmail.com', 
		['nikv96@gmail.com'], fail_silently=False)

def send_to_pres(message):
	send_mail("Periodic Report"
		, message
		, 'allstarscms3003@gmail.com', 
		['nikv96@gmail.com'], fail_silently=False)

def send_to_agency(message):
	send_mail("NOTIFICATION"
		, message
		, 'allstarscms3003@gmail.com', 
		to, fail_silently=False)