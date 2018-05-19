n1=int(input("enter n1"))
l=[]
a=0
for i in range(n1):
    a=int(input("enter value"))
    l.append(a)
l.sort()
candy=0
c=0
for i in range(n1):
    candy=candy+l[i]
print(candy)
