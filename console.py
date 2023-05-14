#!/usr/bin/python3
'''this module has the HBNBCommand class'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''defines the prompt of the console'''

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
