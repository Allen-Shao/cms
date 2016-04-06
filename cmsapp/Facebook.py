import facebook

graph = facebook.GraphAPI(access_token='CAACEdEose0cBAPQsv2jBKxy2Cx4TEYyoDv2YQnPxl0llUuRIvbWoafJXdDB8hYVhHzM8NHW7QnpxZBLz8PI9vESQZBOVtBcrLF81m8az5LrO4fSRgUhrHqzE14qZAJDBZBVmp1rwPijNXeo4ctD0XZAvrPgLraaXChBh5G7mfRi0XZBjnzyfhA1JPClPP1Q2cs08DmZAbUTgwZDZD')

def share_on_facebook(message, description):
    """
    Share the notification on facebook to inform the public

    :param message: The main message
    :param description: Detailed description of the message
    :return: None
    """
    graph.put_wall_post(message="EMERGENCY!!\n\n"+message+"\n\n"+description)

