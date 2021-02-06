l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
f =list(zip(l1,l2))
print(f)
opposites = list(filter(lambda s: len(s[0])>3 and len(s[1])>3, f))
print(opposites)

#2nd Problem
x = int(input())
y = int(input())
z = int(input())

lst = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (x+y+z)!=3 ]
print(lst)
