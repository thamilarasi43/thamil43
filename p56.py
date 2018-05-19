ax1=int(input("enter a-x"))
ay1=int(input("enter a-y"))
bx1=int(input("enter b-x"))
by1=int(input("enter b-y"))
cx1=int(input("enter c-x"))
cy1=int(input("enter c-y"))
dx1=int(input("enter d-x"))
dy1=int(input("enter d-y"))
if ax1==ay1 and ay1==bx1 and by1==cx1 and cx1==cy1 and cy1==dx1 and dy1==ax1:
    print("yes")
else:
    print("no")
