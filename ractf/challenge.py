from .abc import APIBaseObject
from .helpers.requests import post
from .hint import Hint


class Challenge(APIBaseObject):
    def __init__(self, object_id, ctf, data=None):
        self.id = object_id
        self.ctf = ctf
        super(Challenge, self).__init__(ctf, data=data)
        self.convert_json_to_hints()

    def get_api_path(self):
        return f"challenges/{self.id}/"

    def convert_json_to_hints(self):
        hints = []
        for hint in self.hints:
            if isinstance(hint, Hint):
                continue
            hints.append(Hint(hint["id"], self, self.ctf, data=hint))
        self.hints = hints
    
    def submit_flag(self, flag):
        resp = post("challenges/submit_flag/", json={"challenge": self.id, "flag": flag})
        self._fill_attrs()
        return resp["m"] == "correct_flag"