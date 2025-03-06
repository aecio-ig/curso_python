#Count é um iterador sem fim
from itertools import count

c1 = count()
r1 = range(100)

print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))

print('inicio do laçudo')
for i in c1:
    if i > 100:
        break
    print(i)