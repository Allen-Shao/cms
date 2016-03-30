from twilio.rest import TwilioRestClient


def send_sms(message):
	account_sid = "ACb9185852cd063d3a5a1df3cb93314620"
	auth_token  = "23156710162562e7ac98eeedd1120460"
	client = TwilioRestClient(account_sid, auth_token)

	client.sms.messages.create(body=message, to="+6590571662", from_="+15005550006")
