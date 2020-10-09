import sys
import time

from .UserListsHandler import UserListsHandler
from .InputReader import InputReader

def main():
    try:
        args = sys.argv[1:]

        if args[0] == 'run':
            print("- Initializing.. -")
            time.sleep(2.5)
            user_lists_handler = UserListsHandler()
            input_reader = InputReader()
            print("- Running.. -")
            time.sleep(2.5)
            # list_handler.handle(args[2], args[1])
            time.sleep(2.5)
            print(" - Done! -")
    except KeyboardInterrupt as e:
        pass