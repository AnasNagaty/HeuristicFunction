import math
import copy

k = 0
position = ''

n=int(input("Enter N for N x N matrix : ")) 
initial=[]                                                

for i in range(n):     
    row_list=[]  
    for j in range(n): 
        row_list.append(int(input()))           
    initial.append(row_list)  


#initial = [[2, 8, 3],
 #          [1, 6, 4], 
  #         [7, 0, 5]]

goal = [[1, 2, 3],
        [8, 0, 4], 
        [7, 6, 5]]




def SearchGoal(num):
    for i in range(3):
        for j in range(3):
            if(num == goal[i][j]):
                return [i,j]

def searchZero(num, initial):
    for i in range(3):
        for j in range(3):
            if(num == initial[i][j]):
                return [i, j]

def misplaced(initial):
    misplaced = 0

    for i in range(3):
        for j in range(3):
            if initial[i][j] == 0:
                misplaced += 0
            elif initial[i][j] != goal[i][j]:
                misplaced += 1

    return(misplaced)

def manhatten(initial):
    manhatten = 0
    
    for i in range(3):
        for j in range(3):
            if initial[i][j] == 0:
                manhatten += 0
            elif initial[i][j] != goal[i][j]:
                x = SearchGoal(initial[i][j])
                manhatten += abs(x[0] - i) + abs(x[1] - j)

    return(manhatten)



print("\n\n")
print("Initial")
for i in range(n):
    print("| ",end=" ")
    for j in range(n):
        print(initial[i][j], " | ",end=" ")
    print()

print("Misplaced ", misplaced(initial))
print("Manhatten ", manhatten(initial))
print("\n")



def goprint(initial):
 
    print("Moved", position)
    M = copy.deepcopy(initial)
    for x in range(3):
        print("| {one} | {two} | {three} |".format(one=M[x][0], two=M[x][1], three = M[x][2]))
    print("Misplaced ", misplaced(initial))
    print("Manhatten ", manhatten(initial))
    print("\n")
    

def moveleft(initial):
    z = searchZero(0,initial)
    zrow = z[0]
    zcol = z[1]
    temp = initial[zrow][zcol-1]
    initial[zrow][zcol-1] = initial[zrow][zcol]
    initial[zrow][zcol] = temp
    goprint(initial)

def movetop(initial):
    z = searchZero(0, initial)
    zrow = z[0]
    zcol = z[1]
    temp = initial[zrow-1][zcol]
    initial[zrow-1][zcol] = initial[zrow][zcol]
    initial[zrow][zcol] = temp
    goprint(initial)

def moveright(initial):
    z = searchZero(0, initial)
    zrow = z[0]
    zcol = z[1]
    temp = initial[zrow][zcol+1]
    initial[zrow][zcol+1] = initial[zrow][zcol]
    initial[zrow][zcol] = temp
    goprint(initial)

def movebottom(initial):
    z = searchZero(0, initial)
    zrow = z[0]
    zcol = z[1]
    temp = initial[zrow+1][zcol]
    initial[zrow+1][zcol] = initial[zrow][zcol]
    initial[zrow][zcol] = temp
    goprint(initial)



def numberMoves(initial):
    global k
    z = searchZero(0,initial)
    zrow = z[0]
    zcol = z[1]
    if(zrow == 0):
        top = 0
        bottom = 1
        k+= 1
    if(zrow == 1):
        top = 1
        bottom = 1
        k += 2
    if(zrow == 2):
        top = 1
        bottom = 0
        k+= 1


    if(zcol == 0):
        left = 0
        right = 1
        k+= 1
    if(zcol == 1):
        left = 1
        right = 1
        k+= 2
    if(zcol == 2):
        left = 1
        right = 0
        k+= 1

    return [left, top, right, bottom]



moves = numberMoves(initial)
count = 0
next = []

for i in range(k):
    next.append(copy.deepcopy(initial))
if(moves[0] == 1):
    position = 'Left'
    moveleft(next[count])
    count += 1
if(moves[1] == 1):
    position = 'Top'
    movetop(next[count])
    count += 1
if(moves[2] == 1):
    position = 'Right'
    moveright(next[count])
    count +=1
if(moves[3] == 1):
    position = 'Bot'
    movebottom(next[count])
    count +=1

