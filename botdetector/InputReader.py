from .User import User

class InputReader:

    def __init__(self):
        pass

    def read_args(self, command_type: str, args):
        """
        docstring
        """
        def check_for_user():
                """
                docstring
                """
                
                username = args[0]

                try:
                    user = User(username)
                except KeyError as exception:
                    print("Invalid username!")
                    return False

        minimum_lengths = {
            "run": 2
        }

        check_functions = {
            "run": check_for_user
        }

        if len(args) > 0:
            if len(args) < minimum_lengths[command_type]:
                print("Not enough arguments!")
                return False
            if check_functions[command_type]() == False:
                return False

        

        

        