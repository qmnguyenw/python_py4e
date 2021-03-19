import xml.etree.ElementTree as ET
data = '''
    <person>
        <name>QuangNg</name>
        <phone type='intl'>
            0123456789
        </phone>
        <email hide='yes'/>
    </person>
    '''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))