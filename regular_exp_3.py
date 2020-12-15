import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'john@gmail.com'

a = pattern.search(string)
print(a)

# Password checker
# contain any sort letters, numbers $%#@
# has to end with a number
password_pattern = re.compile(r"[a-zA-Z0-9$%#@]{7,}[\d]")
password = 'suspectre%$#8'
b = password_pattern.fullmatch(password)
print(b)