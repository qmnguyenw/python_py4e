import json
import urllib.request, urllib.parse, urllib.error
import ssl

# link
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1075462.json (Sum ends with 66)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# asking user to input url of JSON data file
while True:
    url = input('Enter location: ')
    if len(url) < 1: 
        print('Wrong URL format\n---\n')
        continue

    if url == 'done':
        print('End program')
        break
    
    print('Retrieving', url)
    handle = urllib.request.urlopen(url, context=ctx)
    data = handle.read().decode()
    print('Retrieved', len(data), 'characters')

    # parse data into tree
    try:
        tree = json.loads(data)
    except:
        tree = None

    if not tree:
        print('- Failure To Retrieve -')
        continue

    # print(json.dumps(tree, indent=2))

    numbers = list()

    for comment in tree['comments']:
        # print('number', comment['count'])
        numbers.append(int(comment['count']))

    print(len(numbers))
    print(sum(numbers))