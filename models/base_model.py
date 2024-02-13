#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes:
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """Initializes attributes for class BaseModel
        Args:
            id - identification number
            *args - arguments (not used)
            **kwargs - dictionary arguments
        """

    def __init__(self, *args, **kwargs):
        """Initializes attributes for class BaseModel
        Args:
            id - identification number
            *args - arguments (not used)
            **kwargs - dictionary arguments
            """
        if kwargs and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v,
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a formated string of classname, id, and dictionary
        contens
        """

        return ("[{}]({})({})".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Saves any new information added to a class instance and
        saves an update time
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of all the contens of a class instance"""

        dit = self.__dict__.copy()
        dit['__class__'] = self.__class__.__name__
        dit['updated_at'] = self.updated_at.isoformat()
        dit['created_at'] = self.created_at.isoformat()
        return dit
