from .ApiRequester import ApiRequester

class User():

    def __init__(self, username):
        
        users_api_url = "https://api.roblox.com/users/get-by-username?username={0}".format(username)

        requester = ApiRequester()
        user_info = requester.get(users_api_url, True, None)

        self.username = username
        self.user_id = user_info["id"]
