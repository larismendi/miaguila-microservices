


from flask import current_app
import requests


class PostcodeService():
    @staticmethod
    def postcodes(payload):
        r = requests.get('https://api.postcodes.io/postcodes', params=payload)
        data = r.json()
        return data