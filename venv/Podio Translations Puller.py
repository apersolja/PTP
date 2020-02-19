# coding=utf-8
client_id = "podio-translations-puller"
client_secret = "EQQS1IAeRzTesrVLb4KQSekVdra8lHoqOHScFhnosakjxKvrnMD40Eq7bO03XTkt"
username = "andrej.persolja@creativesolutions.si"
password = "Msc91fcb01"

from pypodio2 import api

#create empty lists
engTranslations = []
dutTranslations = []
espTranslations = []
sloTranslations = []

client = api.OAuthClient(client_id, client_secret, username, password)

#Create empty class for translation items
class TranslationItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

#Loop through items to find relevant data
translations = client.Application.get_items(23043195, limit=500)
for item in translations['items']:
    engTranslation = TranslationItem('', '') #Set empty objects with two parameters into which the keys and values will be written
    dutTranslation = TranslationItem('', '')
    espTranslation = TranslationItem('', '')
    sloTranslation = TranslationItem('', '')
    for field in item['fields']:
        for value in field['values']:
            for innervalue in field['values']:
                if field['label'] == 'String name': #If found item is a String name, add it to stringName as key
                    stringName = innervalue['value']
                    stringName.encode('utf') #encoding because of funny characters in Spanish

                    engTranslation.key = stringName
                    dutTranslation.key = stringName
                    espTranslation.key = stringName
                    sloTranslation.key = stringName

                elif field['label'] == 'English': #define Eng values
                    engValue = innervalue['value']
                    engValue.encode('utf-8')

                    engTranslation.value = engValue

                elif field['label'] == 'Nederlands': #define Dut values
                    dutValue = innervalue['value']
                    dutValue.encode('utf-8')

                    dutTranslation.value = dutValue

                elif field['label'] == u'Español': #define Esp values
                    espValue = innervalue['value']
                    espValue.encode('utf-8')

                    espTranslation.value = espValue

                elif field['label'] == 'Slovensko': #define Slo values
                    sloValue = innervalue['value']
                    sloValue.encode('utf-8')

                    sloTranslation.value = sloValue

    engTranslations.append(engTranslation) # Append found values
    dutTranslations.append(dutTranslation)
    espTranslations.append(espTranslation)
    sloTranslations.append(sloTranslation)

#write everything to separate files
newFile = open('en.txt', 'w+')
for eng in engTranslations:
     newFile.write('"' + eng.key.encode('utf-8') + '"' + ' ' + '=' + ' ' + '"' + eng.value.encode('utf-8') + '"' + '\n')
newFile.close()

newFile = open('esp.txt', 'w+')
for esp in espTranslations:
     newFile.write('"' + esp.key.encode('utf-8') + '"' + ' ' + '=' + ' ' + '"' + esp.value.encode('utf-8') + '"' + '\n')
newFile.close()

newFile = open('dut.txt', 'w+')
for dut in dutTranslations:
     newFile.write('"' + dut.key.encode('utf-8') + '"' + ' ' + '=' + ' ' + '"' + dut.value.encode('utf-8') + '"' + '\n')
newFile.close()

newFile = open('slo.txt', 'w+')
for slo in sloTranslations:
     newFile.write('"' + slo.key.encode('utf-8') + '"' + ' ' + '=' + ' ' + '"' + slo.value.encode('utf-8') + '"' + '\n')
newFile.close()

