inp = []
for lines in open("temp"):
  inp.append(int(lines.strip()))

def part1(inp):
  last = 99999
  tot = 0
  for i in inp:
    if i > last:
      tot += 1
  print(tot)
  return tot

def part2(inp):
  last = 99999
  tot = 0
  val = []
  for i in range(len(inp)-2):
    val.append(inp[i] + inp[i+1] + inp[i+2])
  for i in val(
      
