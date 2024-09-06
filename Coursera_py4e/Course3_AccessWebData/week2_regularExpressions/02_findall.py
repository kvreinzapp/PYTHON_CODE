import re

x = 'hello, i just want more 42 not 24'
y = re.findall('[0-5]+', x)
print(y)
