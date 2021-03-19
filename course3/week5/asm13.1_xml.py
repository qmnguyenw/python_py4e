import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

# link
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1075461.xml (Sum ends with 78)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving:', url)

html = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(html)
comments = tree.findall('comments/comment/count')

total = 0
numbers = list()

for number in comments:
    numbers.append(number.text)
    total += int(number.text)

print(numbers)
print(total)