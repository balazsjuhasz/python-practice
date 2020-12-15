import re

pattern = re.compile('search this')
string = 'search this inside of this text please!'

#print('search' in string)

match = re.search('this', string)
print(match.span())
print(match.start())
print(match.end())
print(match.group())

match2 = pattern.search(string)
print(match2.group())
match3 = pattern.findall(string)
print(match3)
match4 = pattern.fullmatch(string)
print(match4)
match5 = pattern.match(string)
print(match5)