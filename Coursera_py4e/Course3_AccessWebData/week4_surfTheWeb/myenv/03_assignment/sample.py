from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
total = 0
count = 0
for tag in tags:
    total = total + int(tag.text)
    count = count + 1

print('Count', count)
print('Sum', total)

# print(tag.get('class', None))
# Look at the parts of a tag
# print('TAG:', tag)
# print('URL:', tag.get('href', None))
# print('Contents:', tag.contents[0])
# print('Attrs:', tag.attrs)
