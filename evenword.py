str = input("Enter a string:")
lst1 = str.split()
evenlst = []
for word in lst1:
    if (len(word)%2==0):
        evenlst.append(word)
print(evenlst)
