class UserListsHandler:

    followers_api_url = "https://friends.roblox.com/v1/users/{0}/followers"
    friends_api_url = "https://friends.roblox.com/v1/users/{0}/friends"
    followings_api_url = "https://friends.roblox.com/v1/users/{0}/followings"

    valid_list_types = [
        "followers",
        "friends",
        "followings"
    ]

    def __init__(self):
        pass

    def handle(list_type):
        pass