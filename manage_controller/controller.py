#from get import Catdialog,CatCharacterFilter
from manage_api.get import Catdialog, CatCharacterFilter 


class Controllerdialog:
    
    def controller_id(Endpoint:str,name:str):
        name_list = Catdialog.cat_id(Endpoint)
        name_id = ''
        
        for item in name_list:
            print(item['name'])
            if item['name'] == name:
                print(item['name'])
                name_id = item['_id']
        print(name_id)
        return name_id
    
    def controller_dialog(Endpoint, name_id):
        quote = Catdialog.cat_dialog(Endpoint, name_id)
        for dialog in quote:
            print(dialog['dialog'])


class ControllerCharacter:

    @classmethod
    def controller_character(cls,name:str):
        character = CatCharacterFilter.cat_filter_character(name)
        print(character)
        for item in character:
            if item['birth'] == '' or item['birth'] == 'NaN':
                item['birth'] = 'dont exist this information'
            else:
                print(item['birth'])
            if item['death'] == '' or item['death'] == 'NaN':
                item['death'] = 'dont exist this information'
            else:
                print(item['death'])
            if item['race'] == '' or item['race'] == 'NaN':
                item['race'] = 'dont exist this information'
            else:
                print(item['race'])
            if item['realm'] == '' or item['realm'] == 'NaN':
                item['realm'] = 'dont exist this information'
            else:
                print(item['realm'])
            if item['hair'] == '' or item['hair'] == 'NaN':
                item['hair'] = 'dont exist this information'
            else:
                print(item['hair'])
            if item['wikiUrl'] == '' or item['wikiUrl'] == 'NaN':
                item['wikiUrl'] = 'dont exist link for this character'
            else:
                print(item['wikiUrl'])
        return character
        
"""
    _id,race,birth,death,realm,hair, wikiUrl
"""

#Controllerdialog.controller_id('character','Samwise Gamgee')
#id_name = Controllerdialog.controller_id('character','Samwise Gamgee')
#Controllerdialog.controller_dialog('character',id_name)

ControllerCharacter.controller_character('Frodo Baggins')
#ControllerCharacter.controller_character('Boromir')