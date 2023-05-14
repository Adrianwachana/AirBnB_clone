#!/usr/bin/python3
'''this module has the HBNBCommand class'''

import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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

    def do_create(self, arg):
        '''creates a new instance of BaseModel, saves it and prints the id'''
        if not arg:
            print("**class name missing**")
            return

        class_name = arg.strip()
        if class_name not in self.__models:
            print("**class doesn't exist**")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""

        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            print(retrieved_record)
        except Exception:
            pass

    def do_destroy(self, arg):
        """Destroys an instance of a class based on the class name and id."""

        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            storage.destroy(retrieved_record)
        except Exception:
            pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name."""

        if not arg:
            # Print all instances
            instances = storage.all()
            instance_list = []
            for instance in instances.values():
                instance_list.append(str(instance))
            print(instance_list)
        else:
            class_name = arg.strip()
            if class_name not in self.__models:
                print("** class doesn\'t exist **")
                return
            # Print instances of a specific class
            file_storage = storage._FileStorage__objects
            instance_list = []
            for instance in file_storage.values():
                if instance['__class__'] == class_name:
                    instance_list.append(str(instance))
            print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)"""

        args = self.get_update_args(arg)

        if args is None:
            return

        [class_name, instance_id, attribute, value] = args

        try:
            record = self.find_record(class_name, instance_id)

            if record is None:
                print('** no instance found **')
                return

            retrieved_record = globals()[class_name](**record)
            setattr(retrieved_record, attribute, value)
            setattr(retrieved_record, "updated_at", datetime.now())
            storage.new(retrieved_record)
        except Exception:
            pass

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id."""

        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            print(retrieved_record)
        except Exception:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
