from decouple import config

class TokenApi:
    KEY = config('KEY')
    token = f'Bearer {KEY}'

    headers = {
        'Authorization' : token
    }
