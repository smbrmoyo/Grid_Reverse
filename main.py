from pprint import pprint

def print_grid():
    for e in a:
        print("|| " + " | ".join(e) + " || ")

Height = 5
Width = 5
actu_x = 0
actu_y = 0
counter_move = 0

'''for i in range(Height):
    print(" . "*10)
    print(" . "*10)'''

a = [[0 for i in range(Height)] for j in range(Width)]

#print_grid()

for h in a:
    pprint(h)

print("\nStart of the game\n")

a[Width-1][0] = 5
actu_x = Width-1
actu_y = 0
prev_x = Width-1
prev_y = 0
counter_rev = 0
interm_x = 0
interm_y = 0

for h in a:
    pprint(h)

#TODO take X and Y values, store them in variables and use them while player is moving

#USER INPUT

while True:

    if counter_move == 10:
        print("\nNo more chances left!\n")
        break

    move = input("\nMake a move\n")
    move = move.lower()
    if move == "z" and actu_x == 0:
        a[actu_x][actu_y] = 5

    elif move == "z" and actu_x+1 >= 0:
        prev_x = actu_x
        prev_y = actu_y
        a[actu_x][actu_y] = 0
        a[actu_x - 1][actu_y] = 5
        actu_x = actu_x - 1
        actu_y = actu_y

    if move == "q" and actu_y == 0:
        a[actu_x][actu_y] = 5
    elif move == "q" and actu_y-1 >= 0:
        prev_x = actu_x
        prev_y = actu_y
        a[actu_x][actu_y - 1] = 5
        a[actu_x][actu_y] = 0
        actu_x = actu_x
        actu_y = actu_y - 1

    if move == "s" and actu_x == Height-1:
        a[actu_x][actu_y] = 5
    elif move == "s" and actu_x+1 <= Height-1:
        prev_x = actu_x
        prev_y = actu_y
        a[actu_x + 1][actu_y] = 5
        a[actu_x][actu_y] = 0
        actu_x = actu_x + 1
        actu_y = actu_y

    if move == "d" and actu_y == Height-1:
        a[actu_x][actu_y] = 5

    elif move == "d" and actu_y+1 <= Width-1:
        prev_x = actu_x
        prev_y = actu_y
        #a[prev_x][prev_y] = a[actu_x][actu_y]
        a[actu_x][actu_y + 1] = 5
        a[actu_x][actu_y] = 0
        actu_x = actu_x
        actu_y = actu_y + 1

    for h in a:
        pprint(h)

    if actu_x == 0 and actu_y == Width-1:
        print("\nYou won!!!\n")
        break

    if move == "r" and counter_rev == 0:
        a[actu_x][actu_y] = 0
        actu_x = prev_x
        actu_y = prev_y
        a[prev_x][prev_y] = 5
        counter_rev += 1
        #TODO assign actu to prev, swicth values and then assign prev to actu
        #So that: Before rev, Actu 30 and prev 40. After rev, Actu 40 and rev 30

    print("Prev:", prev_x,prev_y, a[prev_x][prev_y])
    print("Actu:", actu_x, actu_y, a[actu_x][actu_y])
    counter_move += 1