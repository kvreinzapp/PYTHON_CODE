import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if (len(url) < 1):
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(0, count + 1):
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)
