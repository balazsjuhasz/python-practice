import re

pattern = re.compile(r"([a-zA-z]).([a])")
string = 'search this inside of this text please!'

a = pattern.search(string)
print(a.group(0))
print(a.group(1))
print(a.group(2))