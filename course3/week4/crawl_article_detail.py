from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')


mainUrl = 'https://www.geeksforgeeks.org/snake-water-gun-game-using-python/'

url = mainUrl
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

titleList = soup.select('#post-534227 > div.title')
print(titleList)

# for title in titleList:
#     if(title['class']!='title'): continue
#     print(title)


aList = soup.find('div', attrs={'class':'code-container'})
aList = soup.select('#highlighter_43411 > table > tbody > tr > td > div')
print(aList)
# for a in aList:
#     if (a['class'] != 'code-container'): continue
#     print(a)
    
