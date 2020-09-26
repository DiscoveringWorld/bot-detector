from .ApiRequester import ApiRequester

class User():

    def __init__(self, user_id):
        
        users_api_url = "https://api.roblox.com/users/{0}".format(user_id)

        requester = ApiRequester()
        user_info = requester.get(users_api_url, True, None)

        self.user_id = user_id
        self.username = user_info["Username"]
