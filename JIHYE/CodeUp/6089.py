sN, pN, rN = input().split()
sN = int(sN)
pN = int(pN)
rN = int(rN)

for i in range(rN-1):
  sN *= pN

print(sN)
