from twilio.rest import TwilioRestClient


def send_sms(contact, message):
    """
    Send sms to the given number

    :param message: The message to be sent to the number
    :return: None
    """
    account_sid = "AC205861da24ebabcdaf9c11c51fed2e13"
    auth_token = "34abeb0f09c29f9632812e079dc97333"
    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(body=message, to="+65"+contact, from_="+14846481449")
    print("SMS has been sent to " + "+65"+contact)