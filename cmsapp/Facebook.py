import facebook

graph = facebook.GraphAPI(access_token='452462581629614', version='2.5')

def shareonfacebook(message, caption, name, description):

	attachment =  {
	    'name': name,
	    'link': 'http://www.example.com/',
	    'caption': caption,
	    'description': description
	}

	graph.put_wall_post(message='Check this out...', attachment=attachment)

