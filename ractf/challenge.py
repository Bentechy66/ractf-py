from .abc import APIBaseObject


class Challenge(APIBaseObject):
    def __init__(self, object_id, ctf, data=None):
        self.id = object_id
        super(Challenge, self).__init__(ctf, data=data)

    def get_api_path(self):
        return f"challenges/{self.id}/"
