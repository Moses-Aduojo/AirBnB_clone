"""
provides the class "BaseModel" that defines all common attributes/methods for
other classes.
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Basemodel: base class for other class
    attributes:
      id: string - assign with an uuid when an instance is created
      created_at: datetime - assign with the current datetime when an instance
      is created
      updated_at: datetime - assign with the current datetime when an
      instance is
      created and it will be updated every time you change your object
    methods:
      save(self): updates the public instance attribute updated_at with
      the current
      datetime
      to_dict(self): returns a dictionary containing all keys/values
      of __dict__ of
      the instance:
    """
    def __init__(self, *args, **kwargs):
        """
        initialize the "id, created_at and updated_at" instances attribute
        at creation or use kwargs for initializtion if provided
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        return [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance:"""
        new_dict = {}
        new_dict.update(self.__dict__)
        new_dict.update({'__class__': self.__class__.__name__})
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
