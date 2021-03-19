import json
import urllib.request, urllib.parse, urllib.error
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        print('Wrong URL format\n---\n')
        continue

    if address == 'done':
        print('End program')
        break

    params = dict()
    params['address'] = address
    if api_key is not False:
        params['key'] = api_key
    
    url = serviceurl + urllib.parse.urlencode(params)
    
    print('Retrieving', url)
    handle = urllib.request.urlopen(url, context=ctx)
    data = handle.read().decode()
    print('Retrieved', len(data), 'characters')

    # transforming data of JSON file to tree
    try:
        tree = json.loads(data)
    except:
        tree = None

    if not tree:
        print('- Failure To Retrieve -')
        continue

    # print(json.dumps(tree, indent=2))

    place_id = tree['results'][0]['place_id']
    print('Place id', place_id)
    print('---')