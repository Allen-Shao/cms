import facebook

access_token = "CAACEdEose0cBADGMIlrwZBxcLZA1qKZCn1fXbWtY5MWWgZAJxoWIhGM0ZAz59ZBzBaEtKfOIiKIngg7WyI5XROARjfaWeNzsSdAwLXUoRXss3XXKi6mBUaf9WftXlZALvbcBkMFPvqu8234Qyh0FXNWkys9Sml4ssB9jafWDjhkZAGW5ga8eefGwbg9p1KlD22ZBdUeAuixdKdAZDZD"
graph = facebook.GraphAPI(access_token=access_token)

def share_on_facebook(message, description):
    """
    Share the notification on facebook to inform the public

    :param message: The main message
    :param description: Detailed description of the message
    :return: None
    """
    graph.put_wall_post(message=message+"\n\n"+description)

