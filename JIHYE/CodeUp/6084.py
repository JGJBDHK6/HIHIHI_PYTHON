﻿h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

wav = h * b * c * s / 8 / 1024 / 1024

print("%.1f MB" %wav)
