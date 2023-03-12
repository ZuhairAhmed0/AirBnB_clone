#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    """ BaseModel that defines all common attributes/
    methods for other classes """

    def __init__(self, *arg, **kwargs):
        """Public instance artributes initialization
        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.item():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.now()
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
