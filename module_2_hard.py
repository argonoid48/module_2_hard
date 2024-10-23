# Галкин Андрей
# Задание "Слишком древний шифр"

import random
n = random.randint(3, 20)
parol = []
for x in range (1, int(n/2)+1):
    for y in range (2, n):
        if x + y > n:
            break
        elif x == y:
            continue
        elif n % (x+y) == 0:
            parol.append(x)
            parol.append(y)
print(n, '- ', parol)