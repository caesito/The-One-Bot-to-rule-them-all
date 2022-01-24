#from api_token import key
from decouple import config
import requests




class Catdialog:
    KEY = config('KEY')
    token = f'Bearer {KEY}'

    headers = {
        'Authorization' : token
    }

    endpoint = ''
    url_api = 'https://the-one-api.dev/v2/'

    @classmethod
    def cat_id(cls, camp1: str):
        

        cls.endpoint = camp1
        url = f'{cls.url_api}' + f'{cls.endpoint}'
        response = requests.get(url=url,headers=cls.headers)
        resp = response.json()
        print(url)
        print(response.status_code)
        book = resp['docs'] # return a list of Dicts
        print(resp)
        return book

        #print(book)
        

    
    @classmethod
    def cat_dialog(cls,endpoint:str, name_id:str):
        
        url_2 = f'{cls.url_api}' + f'{endpoint}/{name_id}'

        response_2 = requests.get(url=url_2,headers=cls.headers)
        resp_2 = response_2.json()
        quote_name = resp_2['docs']
        print(response_2.status_code)
        print(quote_name)
        return quote_name

    @classmethod
    def cat_chapter(cls, endpoint_book, id_book):
        cls.endpoint = endpoint_book
        url = f'{cls.url_api}' + f'{cls.endpoint}/{id_book}'
        response = requests.get(url= url, headers= cls.headers)
        resp = response.json()
        print(response.status_code)
        return print(resp)


class CatCharacterFilter(Catdialog):

    @classmethod
    def cat_filter_character(cls, name:str):
        cls.endpoint = 'character'
        url = f'{cls.url_api}' + f'{cls.endpoint}?name={name}'
        response = requests.get(url=url,headers=cls.headers)
        resp = response.json()
        character = resp['docs']
        return character

"""
    /chapter?name=name
    /chapter/id_book -> one specifc book
    chapter one -> '5cf5805fb53e011a64671582'
"""

#Catdialog.cat_id("character")
#Catdialog.cat_chapter('chapter','5cf5805fb53e011a64671582' )
#Catdialog.cat_dialog('chapter', '5cf5805fb53e011a64671582')
#Catdialog.cat_filter_character('Gandalf')