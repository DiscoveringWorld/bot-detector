import sys

from .UserListsHandler import UserListsHandler

def main():
    args = sys.argv[1:]

    if args[0] == 'run':
        list_handler = UserListsHandler()

        list_handler.handle(args[2], args[1])

# user_id = args[1]

# user = User(user_id)
# requester = ApiRequester()

# url = followers_api_url.format(user.user_id)
# user_list = requester.get(url, True, {'limit': 100})

# number_of_bots = 0

# for user in followers["data"]:
#     follower_user = User(follower["id"])

#     users_api_url = "https://users.roblox.com/v1/users/{0}/status".format(follower_user.user_id)
#     user_status_info = requester.get(users_api_url, True, None)

#     bot_description = BotDescription()
#     bot_text = bot_description.return_description()

#     print("{0}: {1}".format(follower_user.username, user_status_info["status"]))
#     if ',' in user_status_info["status"]:
#         if user_status_info["status"][:user_status_info["status"].index(',')] in bot_text:
#             number_of_bots += 1
#     elif '!' in user_status_info["status"]:
#         if user_status_info["status"][:user_status_info["status"].index('!')] in bot_text:
#             number_of_bots += 1

# print("{0} has {1} bots as a follower.".format(user.username, number_of_bots))