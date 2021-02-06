str = input("Enter a string: ")
dict = {}

for i in str:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1

print(dict)

x1= input("Enter the character or the word to be removed:")

del dict[x1]
print(dict)    
