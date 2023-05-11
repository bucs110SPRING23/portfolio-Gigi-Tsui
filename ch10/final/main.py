from apigenshincharacter import GenshinCharacterapi
from apitranslate import Translaterapi

genshin = GenshinCharacterapi()
Translaterapi = Translaterapi()

characters = genshin.get()

while(1):
    char = int(input('Choose a Number from 1 to 56:'))
    print(characters[char-1],' -> ',Translaterapi.translate(characters[char-1]))

