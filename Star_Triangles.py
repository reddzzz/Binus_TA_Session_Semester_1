n = int(input("insert a number:"))
for i in range (1, n+1):
    print("*" * i)

n = int(input("insert a number:"))
for i in range (1, n +1):
    print("*" * (n + 1 - i))

n = int(input("insert a number:"))
for i in range (1, n+1):
    print(" " *(n-i) + "*" * i)

n = int(input("insert a number:"))
for i in range (1, n+1):
    print((n-i)* " " + i * "* " )

n = input("insert number 1")
n = int(n)
for row in range(0,n,1):
    for col in range(0,n,1):
        if col < row:
            print(" ", end="")
        else:
            print("*", end="")
    print("")

n = int(input("insert a number:"))
x = 0
y = int(n/2) + 1
for i in range (0, n):
    Nst = i + 1
    Nsp = n - Nst
    for a in range(0, Nsp):
        print(" ", end="")
    for b in range(0, Nst + x):
        print("*", end="")
    x=x+1
    print("")
for o in range(0,n):
    Nsp2 = o + 1
    Nst2 = n - Nsp2
    for c in range(0, Nsp2):
        print(" ", end="")
    for d in range(0, Nst2 + y):
        print("*", end="")
    y = y - 1
    print("")
