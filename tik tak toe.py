area, game, pl = ["a", "b", "c", "d", "e", "f", "g", "h", "i"], 1, "X"

def menu():
    print(area[0], " | ", area[1], " | ", area[2], " | ", "\n",
          area[3], " | ", area[4], " | ", area[5], " | ", "\n",
          area[6], " | ", area[7], " | ", area[8], " | ", "\n\n")
while game == 1:
    menu()
    choice = str(input("Where? "))
    area[area.index(choice)] = pl

    if pl == "X":
        pl = "0"
    else:
        pl = "X"

    if area[0] == area[1] == area[2]:
        game = 0

    if area[3] == area[4] == area[5]:
        game = 0

    if area[6] == area[7] == area[8]:
        game = 0

    if area[2] == area[4] == area[6]:
        game = 0

    if area[0] == area[3] == area[6]:
        game = 0

    if area[1] == area[4] == area[7]:
        game = 0

    if area[0] == area[4] == area[8]:
        game = 0

    if area[2] == area[5] == area[8]:
        game = 0
if pl == "X":
    pl = "0"
else:
    pl = "X"
print(f"game over, {pl} won")