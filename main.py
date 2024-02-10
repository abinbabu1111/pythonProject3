m = int(input("enter the no.of rows = "))
n = int(input("enter the no.of  columns n= "))


for i in range(n):
    if i == 0:

        if (n % 2) == 0:
            x = n // 2
        else:
            x = n - n // 2

for j in range(x):
    print(r" ___    ", end='')
    if j == x:
        break
print()
for j in range(x):
    print(r'/   \___', end='')
    if j == x - 2:
        print('/   \\', end='')
        break
print()
for j in range(x):
    print(r'\___/   ', end='')

for j in range(m-1):
    print()
    for j in range(x):
        print(r'/   \___', end='')
        if j == x - 2:
            print('/   \\', end='')
            break
    print()
    for j in range(x):
        print(r'\___/   ', end='')
