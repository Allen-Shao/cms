import facebook

graph = facebook.GraphAPI(access_token='CAACEdEose0cBALuxYhTH9ZBxGeeWaPHUUd2odkg0kGOwxso5lGZBZAHmy7wpc2cssP3LKxJ5kiy6jrfBdaDrulZCsDkqQzP7rxaIFfhF4mJbuMZCLsMsXeSYRiqjNhwvkoZBpaQHFFZAsW4K8vOW9ZBZB5FNJZBu21S6uohEOG3wAaHduwwMb6c1NBQ8kkt77uaJ9p6qEzmiC8MwZDZD')

def share_on_facebook(message, description):
    """
    Share the notification on facebook to inform the public

    :param message: The main message
    :param description: Detailed description of the message
    :return: None
    """
    graph.put_wall_post(message="EMERGENCY!!\n\n"+message+"\n\n"+description)

