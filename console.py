#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        """Display help message for quit command"""
        print("Quit command to exit the program.")
        print()

    def help_EOF(self):
        """Display help message for EOF command"""
        print("EOF command to exit the program.")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

