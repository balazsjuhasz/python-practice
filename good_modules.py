from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

print(datetime.time())
print(datetime.time(5, 45, 2))
print(datetime.date.today())

arr = array('i', [1, 2, 3])

print(arr[0])
