class InputReader:

    def __init__(self):
        pass

    def read_args(self, command_type: str, args: list):
        """
        docstring
        """
        
        minimum_lengths = {
            "run": 2
        }

        if len(args) < minimum_lengths[command_type]:
            print("Not enough arguments!")
            return False