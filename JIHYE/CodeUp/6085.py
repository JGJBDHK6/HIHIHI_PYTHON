w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

bmp = w * h * b / 8 / 1024 / 1024

print("%.2f MB" %bmp)
