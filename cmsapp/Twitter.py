import twitter
api = twitter.Api(consumer_key='Q9TOD65OJ6faFrqizhjAvnPaE',
                  consumer_secret=' ytV8LUtA7Q9xJdVfUe9NKlS46rBtr3gsGXYWR7XXALhZNxXGpP',
                  access_token_key='2997098035-6cPjdMExmBcSrrC37SWFx8qE7Zmp0TzJaYHutVK',
                  access_token_secret='CYCUVLlkmNPnrPV2Kfm1JKJyxtMgc9uLM1Wximz1ROka5')

def postontwitter(message):
	api.PostUpdate(message)