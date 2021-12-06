import numpy as np
inp = []
for i in open('input'):
    a = i.split()
    startx, starty = a[0].split(',')
    startx, starty = int(startx), int(starty)
    endx, endy = a[2].split(',')
    endx, endy = int(endx), int(endy)
    
    inp.append([startx,starty,endx,endy])

arr = np.zeros((1000,1000))

for i in inp:
    if i[1] != i[3] and i[0] != i[2]:
        incx = i[0] < i[2]
        incy = i[1] < i[3]
        length = abs(i[1] - i[3]) + 1
        x,y = i[0], i[1]
        for i in range(length):
            arr[y][x] += 1
            if incx:
                x += 1
            else:
                x -= 1
            if incy:
                y += 1
            else:
                y -= 1
    else:
        ydir = 1
        xdir = 1
        if i[1] > i[3]:
            ydir = -1
        if i[0] > i[2]:
            xdir = -1
        for y in range(i[1], i[3]+1*ydir, ydir):
            for x in range(i[0],i[2]+1*xdir, xdir):
                arr[y][x] += 1

tot = 0
for y in range(1000):
    for x in range(1000):
        if arr[y][x] >= 2:
            tot += 1
print(arr)
print(tot)
