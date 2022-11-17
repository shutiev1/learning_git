import random
i = 0
b = []
while i < 10:
    b.append(random.randint(1,10))
    i += 1
b = tuple(b)
print('max = ', max(b),'и',  'min = ', min(b))