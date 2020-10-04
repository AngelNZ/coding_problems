sides,h,v = map(int,input().split())

if h < (sides/2.0):
    h = sides-h
if v < (sides/2.0):
    v = sides-v
piece = h*v*4

print(piece)