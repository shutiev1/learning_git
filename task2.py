import random
tuple1 = tuple(random.randint(0, 5) for i in range(10))
tuple2 = tuple(random.randint(-5, 0) for i in range(10))
tuple3 = tuple1 + tuple2

count = 0
for i in tuple3:
    if i == 0:
        count += 1
print("кортеж:", tuple3)
print("количество нулей:", count)