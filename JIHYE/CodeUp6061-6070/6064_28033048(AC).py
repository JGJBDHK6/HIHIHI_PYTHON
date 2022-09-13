a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

v = (a if a < b else b) if ((a if a < b else b) < c) else c

print(v)
