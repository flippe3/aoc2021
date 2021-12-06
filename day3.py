inp = []
for i in open("input"):
    a = i.split()
    inp.append(a[0])


def most_common(inp, index):
    ans = [0,0]*len(inp[0])
    for i in inp:
        for j in range(len(i)):
            if i[j] == "0":
                ans[j*2] += 1
            else:
                ans[j*2+1] += 1
    if ans[index*2] > ans[(index*2)+1]:
        return "0"
    return "1"

def least_common(inp, index):
    ans = [0,0]*len(inp[0])
    for i in inp:
        for j in range(len(i)):
            if i[j] == "0":
                ans[j*2] += 1
            else:
                ans[j*2+1] += 1
    if ans[index*2] <= ans[(index*2)+1]:
        return "0"
    return "1"


def update_inp(inp, criteria):
    new_inp = []
    ele = 0
    remove = []
    for i in inp:
        for j in range(len(criteria)):
            if i[j] != criteria[j]:
                remove.append(ele)
                break
        ele += 1
    for i in range(len(inp)):
        if i not in remove:
            new_inp.append(inp[i])
    return new_inp

index = 0
criteria = ""
ox, lif = 0,0
for i in range(len(inp)):
    criteria += most_common(inp, i)
    inp = update_inp(inp, criteria)
    if len(inp) <= 1:
        print("Most common", int(inp[0], 2))
        ox = int(inp[0], 2)
        break

inp = []
for i in open("input"):
    a = i.split()
    inp.append(a[0])

index = 0
criteria = ""
for i in range(len(inp)):
    criteria += least_common(inp, i)
    inp = update_inp(inp, criteria)
    if len(inp) <= 1:
        print("Least common:", int(inp[0], 2))
        lif = int(inp[0], 2)
        break

print(ox * lif)