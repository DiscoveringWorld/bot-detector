import sys
import time

from .UserListsHandler import UserListsHandler
from .InputReader import InputReader

def main():
    try:
        print("- Initializing.. -")

        args = sys.argv[1:]

        if len(args) > 0 and args[0]:
            user_lists_handler = UserListsHandler()
            input_reader = InputReader()
            
            if input_reader.read_args(args[0], args[1:]) == False:
                return

            time.sleep(2.5)

            print("- Running.. -")
            
            user_lists_handler.handle(args)
            
            time.sleep(2.5)
            
            print("- Done! -")
            return
        print("No values inputed!")
    except KeyboardInterrupt as e:
        pass