from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# link
# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_1075459.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

number_list = list()

# Retrieve all of the td tags
tags = soup('span')

for tag in tags:
    # Look at the parts of a tag
    if tag.attrs == {'class': ['comments']}:
        number_list.append(int(tag.contents[0]))

# print(number_list)
print(sum(number_list))