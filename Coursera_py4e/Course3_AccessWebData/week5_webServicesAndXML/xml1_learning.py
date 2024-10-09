import xml.etree.ElementTree as ET

data = ''' 
<person>
    <name>Klaus</name>
    <phone type="intl">
        +8616622909011
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
