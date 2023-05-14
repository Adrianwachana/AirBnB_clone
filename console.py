#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

def do_quit(self, arg):
    '''exit the program'''
    return True

def do_EOF(self, arg):
    '''Exit the program'''
    print()
    return True

def emptyline(self):
    '''Do nothing for an empty line'''
    pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()