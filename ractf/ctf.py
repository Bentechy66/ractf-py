from .challenge import Challenge
from .helpers.requests import get

class CTF:
    def __init__(self, api_base):
        self.api_base = api_base
        self.auth_token = None

    def get_challenges(self):
        resp = get("challenges/categories/", self)
        challenges = []
        for category in resp["d"]:
            for challenge in category["challenges"]:
                challenges.append(Challenge(challenge["id"], self, data=challenge))
        return challenges
