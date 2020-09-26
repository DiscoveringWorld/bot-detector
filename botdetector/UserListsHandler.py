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
            "followers": UserListsHandler.followers_func,
            "friends": UserListsHandler.friends_func,
            "followings": UserListsHandler.followings_func
        }

        return link_functions

    def followers_func(self):
        print("Followers function called!")

    def friends_func(self):
        print("Friends function called!")

    def followings_func(self):
        print("Followings function called!")

    def __init__(self):
        pass

    def handle(self, list_type):
        
        link = self.user_links[list_type]

        function = self.link_functions[list_type]
        function()

