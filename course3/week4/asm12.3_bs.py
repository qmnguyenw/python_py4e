import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# link
# Sample problem: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual problem: http://py4e-data.dr-chuck.net/known_by_Maca.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User input data
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# create a name list
name_list = list()
print('Retrieving:', url)

for i in range(count):
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    name_list.append(tags[position-1].contents[0])
    url = tags[position-1].get('href', None)
    print('Retrieving:', url)

print(name_list)