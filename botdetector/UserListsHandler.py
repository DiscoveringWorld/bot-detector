from .ApiRequester import ApiRequester
from .User import User
from .BotDescription import BotDescription

class UserListsHandler:

    followers_api_url = "https://friends.roblox.com/v1/users/{0}/followers"
    friends_api_url = "https://friends.roblox.com/v1/users/{0}/friends"
    followings_api_url = "https://friends.roblox.com/v1/users/{0}/followings"

    user_links = {
        "followers": followers_api_url,
        "friends": friends_api_url,
        "followings": followings_api_url
    }

    def return_link_functions(self):
        link_functions = {
            "followers": self.followers_func,
            "friends": self.friends_func,
            "followings": self.followings_func
        }

        return link_functions

    def followers_func(self, user):
        requester = ApiRequester()

        url = self.followers_api_url.format(user.user_id)
        user_list = requester.get(url, True, {'limit': 100})

        number_of_bots = 0

        for user in user_list["data"]:
            other_user = User(user["name"])

            if other_user.criteria() == True:
                number_of_bots += 1

        return number_of_bots

    def friends_func(self, user):
        requester = ApiRequester()

        url = self.friends_api_url.format(user.user_id)
        user_list = requester.get(url, True, {'limit': 100})

        number_of_bots = 0

        for user in user_list["data"]:
            other_user = User(user["name"])

            if other_user.criteria() == True:
                number_of_bots += 1

        return number_of_bots

    def followings_func(self, user):
        requester = ApiRequester()

        url = self.followings_api_url.format(user.user_id)
        user_list = requester.get(url, True, {'limit': 100})

        number_of_bots = 0

        for user in user_list["data"]:
            other_user = User(user["name"])

            if other_user.criteria() == True:
                number_of_bots += 1

        return number_of_bots

    def __init__(self):
        pass

    def handle(self, list_type, user_id):
        user = User(user_id)

        function = self.return_link_functions()[list_type]

        bots = function(user)
        print("{0} has {1} bots as a {2}.".format(user.username, bots, list_type[:-1]))

