from apigenshincharacter import GenshinCharacterapi
from apitranslate import Translaterapi

genshin = GenshinCharacterapi()
Translaterapi = Translaterapi()

characters = genshin.get()

while(1):
    index = int(input('Choose a Number from 1 to 56:'))
    print(characters[index-1],' -> ',Translaterapi.translate(characters[index-1]),'\n')
