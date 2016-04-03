import twitter

def post_on_twitter(message):
    """
    Post the given message on twitter

    :param message: The message to be tweeted
    :return: None
    """
    api = twitter.Api(consumer_key='3stEJXIAniL9suX2kr2VZiXTa',
                      consumer_secret='HBMsON2iHg6UGoCZ1o1WpsOQYlrrKIwssIQLrib6XunxMhQZU3',
                      access_token_key='713015202682253312-iXDC2g0FHosO26tdO6ZuSh402LjJoGS',
                      access_token_secret='gNKCMOBfG6z4IlhRqFG8GqRTH947s7HtmwicX7YsVo5Up')
    api.PostUpdate(message)
