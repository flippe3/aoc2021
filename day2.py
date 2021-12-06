inp = []
for i in open("input"):
    a = i.split()
    inp.append([a[0], int(a[1])])

h,d,a = 0,0,0
for i in inp:
    if i[0] == 'forward':
        h += i[1]
        d += i[1] * a
    elif i[0] == 'down':
        a += i[1]
    elif i[0] == 'up':
        a -= i[1]
print(abs(d*h))