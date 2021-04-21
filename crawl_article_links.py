from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import html2text
import time

def crawlArticleDetail(fname, link):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # url = input('Enter - ')


    # link = 'https://www.geeksforgeeks.org/snake-water-gun-game-using-python/'

    h = html2text.HTML2Text()
    h.ignore_links = True

    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('article')
    id = ''
    for tag in tags:
        id = tag.get('id', None)

    id = "#"+id

    title = ''
    try:
        titleList = soup.select('div.title')
        title = h.handle(str(titleList[0])).replace('`', '')
        # print(h.handle(str(titleList[0])).replace('`', ''))
    except:
        title = 'Empty title'
        print('Empty title')

    content = ''
    try:
        desList = soup.select(id+' > div.text > p')
        content = h.handle(str(desList[0])).replace('`', '')
        # print(h.handle(str(desList[0])).replace('`', '')
    except:
        content = 'Empty content'
        print('Empty content')

    f = open(fname+".py", "w", encoding='utf-8')
    f.write(title + content)



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# mainUrl = 'https://www.geeksforgeeks.org/easy/python/'
# mainUrl = 'https://www.geeksforgeeks.org/basic/python/'
# mainUrl = 'https://www.geeksforgeeks.org/medium/python/'
mainUrl = 'https://www.geeksforgeeks.org/hard/python/'
# mainUrl = 'https://www.geeksforgeeks.org/expert/python/'

i = 1

while True:

    if i == 34: break

    url = mainUrl+str(i)

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    aList = soup.select('div > div > div > div > div > div > div > div > a')

    countLink = 1
    for a in aList:
        if (countLink==21): break
        if (countLink%5==0): time.sleep(0.25)
        print(str(i)+"."+str(countLink),'-',a['href'])
        crawlArticleDetail(str(i)+"_"+str(countLink), a['href'].strip())
        
        countLink=countLink+1
    
    i = i + 1