r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
cnt3 = 0

for ir in range(r):
  for ig in range(g):
    for ib in range(b):
      print(ir,ig,ib)
      cnt3 += 1

print(cnt3)
