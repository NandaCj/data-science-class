import re

p = "  num 123m 1231, nnjn 234m , 3423, 23123 name "

print(re.findall(r'[0-9]+', p))

print(re.sub(r'[a-z]+', 'xxxxxx', p))


k = "maid nandha.paramasivam@gmail.com, sounder.1992@yahoo.com"

print(re.findall(r'.*@.*', k))