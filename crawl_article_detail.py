from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import html2text

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')


mainUrl = 'https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/'

h = html2text.HTML2Text()
h.ignore_links = True

url = mainUrl
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('article')
id = ''
for tag in tags:
    id = tag.get('id', None)

id = "#"+id
print(id)

print('Title:')
title = ''
try:
    titleList = soup.select('div.title')
    title = h.handle(str(titleList[0])).replace('`', '')
    # print(h.handle(str(titleList[0])).replace('`', ''))
except:
    print('Empty title')

content = ''
print('Description:')
try:
    desList = soup.select(id+' > div.text > p')
    content = h.handle(str(desList[0])).replace('`', '')
    # print(h.handle(str(desList[0])).replace('`', '')
except:
    print('Empty description')
# plainCode = soup.find('div', attrs={'class':'code-container'}).text

# # print(plainCode)

# print('\nCode:')
# try:
#     blockCode = soup.select('td.code')
#     print(h.handle(str(blockCode[0])).replace('`', ''))
# except:
#     print('Empty code')

fname = title.replace('/','_')

f = open(fname[:10]+".py", "w")
f.write(title + content)