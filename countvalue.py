str = input("Enter a string: ")
dict = {}
for i in str:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1
print(dict)
count = 0
for  k , v in dict.items():
    count = count+v

print(count)
