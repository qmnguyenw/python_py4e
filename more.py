import webbrowser
import time

count = 0

url_list = list()

# url_list.append('https://www.codegrepper.com/code-examples/python/how+to+open+a+new+incognito+browser+with+webbrowser+python')
fh = open(file='file.txt', mode='r', encoding='utf-8')
for line in fh:
    if line.startswith('http'):
        url_list.append(line)
    else:
        continue
print(url_list)
# # firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s -private-window'
firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s --private'
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
for url in url_list:
    count += 1
    if count % 10 != 0:
        webbrowser.get(firefox_path).open(url)
        # webbrowser.get(chrome_path).open(url)
    else:
        webbrowser.get(firefox_path).open(url)
        time.sleep(30)