from .ApiRequester import ApiRequester
from .BotDescription import BotDescription

class User():

    def __init__(self, username):
        
        users_api_url = "https://api.roblox.com/users/get-by-username?username={0}".format(username)

        requester = ApiRequester()

        code = requester.get(users_api_url, False, None)

        if code == 404:
            return False
        
        user_info = requester.get(users_api_url, True, None)

        self.username = username
        self.user_id = user_info["Id"]

    def criteria(self):
        try:
            requester = ApiRequester()

            if 'ADMIN' in self.username:
                return True
            else:
                users_api_url = "https://users.roblox.com/v1/users/{0}/status".format(self.user_id)
                user_status_info = requester.get(users_api_url, True, None)

                bot_description = BotDescription()
                bot_text = bot_description.return_description()

                print("{0}: {1}".format(self.username, user_status_info["status"]))

                for link in bot_text:
                    if user_status_info["status"].find(link) != -1:
                        return True
                        break
        except NameError as e:
            print(str(e))
