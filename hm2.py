import re
a = input('Введите текст: ')
st = re.sub(r'[^\w\s]', ' ', a)
print(st)
