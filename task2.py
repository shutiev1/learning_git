import random
tuple1 = tuple(random.randint(0, 5) for i in range(10))
tuple2 = tuple(random.randint(-5, 0) for i in range(10))
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple3.count(0))
