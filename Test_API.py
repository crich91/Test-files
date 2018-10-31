import requests, os, sys, time, json, urllib
from io import BytesIO
from PIL import Image
from datetime import datetime

BungieURL = 'https://www.bungie.net'
URL_BASE = 'https://www.bungie.net/Platform'
path = '/GroupV2/GetAvailableAvatars/'
url = URL_BASE + path


API_KEY =  os.environ.get('D2')
headers = {'X-API-Key': API_KEY}
session = requests.Session()
print("Header: {}\n URL: {}\n API: {}\n".format(headers, url, API_KEY ))


response = requests.get(url=url, headers=headers)


print(response)

print("Error Status: {}".format(response.json()['ErrorStatus']))



avatar_list = []
for avatar in response.json()['Response']:
    avatar_list.append(avatar)
list_of_Images = []
for image in avatar_list:
    list_of_Images.append(response.json()['Response'][str(image)])


for i in list_of_Images:
    imgURL = BungieURL + i
    response = requests.get(url=imgURL, headers=headers)
    img = Image.open(BytesIO(response.content))
    #img.show()






'''
for saleItem in response_json['Response']['Data']['saleItemCategories']:
    thesaleitems = saleItem[saleItems]
    for item in thesaleitems:
        hashid = str(item['item']['itemHash'])
        print(hashid)
'''

#print(r)
#print(r['ErrorStatus'])
