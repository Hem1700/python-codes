str = input("Enter a string : ")
dict = {}

for i in str:
    if i not in dict:
        dict[i] = 0
    dict[i]+=1
print(dict)

common_lst = []
keys = list(dict.keys())
for i in keys:
    if dict[i]>1:
        common_lst.append(i)
print(common_lst)
