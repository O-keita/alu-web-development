#!/usr/bin/python3
from datetime import datetime
import uuid
from models import storage

class BaseModel:

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':

                    if key in ['created_at', 'updated_at']:

                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                    self.id = str(uuid.uuid4())

                setattr(self, key, value)


        else:

            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    

    def to_dict(self):

        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.created_at.isoformat()
        return obj_dict


newmodel = BaseModel()
newmodel.save()

print(newmodel)
