#!/usr/bin/python3

import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to the provided filename.
        
        Args:
            filename (str): The name of the file to save the serialized object.
        
        Returns:
            None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from the provided filename.
        
        Args:
            filename (str): The name of the file to load the serialized object from.
        
        Returns:
            CustomObject or None: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Error: The deserialized object is not of type CustomObject.")
                    return None
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
