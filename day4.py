import numpy as np
order = "10,80,6,69,22,99,63,92,30,67,28,93,0,50,65,87,38,7,91,60,57,40,84,51,27,12,44,88,64,35,39,74,61,55,31,48,81,89,62,37,94,43,29,14,95,8,78,49,90,97,66,70,25,68,75,45,42,23,9,96,56,72,59,32,85,3,71,79,18,24,33,19,15,20,82,26,21,13,4,98,83,34,86,5,2,73,17,54,1,77,52,58,76,36,16,46,41,47,11,53".split(',')
#order = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1".split(',')
order = list(map(int, order))

inp = []
temp = []
for i in open("input"):
    a = []
    for j in i.strip().split():
        a.append(np.array(int(j)))
    if len(a) != 0:
        temp.append(np.array(a))      
    else:
        inp.append(np.array(temp))
        temp = []

def check(row, order):
    if np.isin(row, order).all():
        return True
    return False

wins = []

def check_win(inp, order):
    for j in range(5, len(order)):
        for row in range(5):
            if check(inp[row], order[:j]):
                return i, j
        for col in range(5):
            if check(inp[:,col], order[:j]):
                return i, j 
    return -1, -1

heighest = -12
table = None
for i in inp:
    temp1, temp2 =  check_win(i, order)
    if temp2 != -1 and temp2 > heighest:
        table = temp1
        heighest = temp2
    
def unmarked(table, order):
    tot = 0
    for row in range(5):
        for col in range(5):
            if table[row][col] not in order:
                tot += table[row][col]
    return tot

print(table, order[heighest-1])
print("Answer:", unmarked(table, order[:heighest]) * order[heighest-1])
