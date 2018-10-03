import random

li = []

x = 0
y = 0

file = open("data.txt", "r")
content = file.read().split("\n")
for row in range(0,8):
    f = content[row].split(",")
    li.append([])
    for col in range(len(f)):
        if f[col] == "0":
            print("o", end="  ")
            li[row].append("o")
        elif f[col] == "1":
            print("X", end="  ")
            li[row].append("o")
            x = col
            y = row
        elif f[col] == "2":
            print("#", end="  ")
            li[row].append("#")


    print(" ")

for i in range (0,8):
    if content[i] == "0":
        li[y][x] = "o"
    if content[i] == "2":
        li[y][x] = "#"

def chance():
    probability = random.randint(0, 5)
    if probability == 0:
        print("POKEMON,POKEMON, THERE'S A POKEMON!!")

print("HELLO POKEWORLD")
print('''
=============
    MENU
==============
1) Move up
2) Move down
3) Move left
4) Move right
5) Save & End Game
 ''')

while True:
    n = int(input("Please choose a number from 1 to 5: "))
    if n == 1:
        if (y - 1 >= 0):
            y -= 1
    elif n == 2:
        if (y + 1 <= 7):
            y += 1
    elif n == 3:
        if (x - 1 >= 0):
            x -= 1
    elif n == 4:
        if (x + 1 <= 7):
            x += 1
    elif n == 5:
        file = open("data.txt", "w")
        temp = ""
        for i in range(len(li)):
            for j in range(len(li[i])):
                if i == y and j == x:
                    temp += "1"
                elif li[i][j] == "o":
                    temp += "0"
                elif li[i][j] == "#":
                    temp += "2"

                if j < len(li[i]) - 1:
                    temp += ","
            temp += "\n"

        if li[y][x] == "#":
            temp += "2"
        else:
            temp += "0"

        file.write(temp)
        file.close()
        break

    if (li[y][x] == "#"):
        chance()

    for i in range(len(li)):
        for j in range(len(li[i])):
            if i == y and j == x:
                print("X", end="  ")
            elif li[i][j] == "o":
                print("o", end="  ")
            elif li[i][j] == "#":
                print("#", end="  ")
        print(" ")
