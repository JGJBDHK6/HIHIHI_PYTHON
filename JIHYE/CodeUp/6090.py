sN, dN, pN, rN = input().split()
sN = int(sN)
dN = int(dN)
pN = int(pN)
rN = int(rN)

num0 = sN

for i in range(rN-1):
  num0 *= dN
  num0 += pN

print(num0)
