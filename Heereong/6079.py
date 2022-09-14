n = int(input())
s = 0
t = 0

for i in range(1, 1000) :
  s += i
  t = i
  if s >= n :
    print(t)
    break
