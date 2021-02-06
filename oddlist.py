A=[]
n=int(input("Enter the size of the  List ::"))
print("Enter the Element of   List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)



def splitevenodd(A):
   evenlist = []
   oddlist = []
   for i in A:
      if (i % 2 == 0):
         evenlist.append(i)
      else:
         oddlist.append(i)
   print("Even lists:", evenlist)
   print("Odd lists:", oddlist)

splitevenodd(A)
