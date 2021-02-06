str1 = input("Enter first string: ")
dict1 = {}
for i in str1:
    if i not in dict1:
        dict1[i] = 0
    dict1[i]+=1
print(dict1)
str2 = input("Enter second string: ")
dict2 = {}
for i in str2:
    if i not in dict2:
        dict2[i] = 0
    dict2[i]+=1
print(dict2)
print("*****************************")
def f(dict1 , dict2):
    return (dict2.update(dict1))
print(f(dict1 , dict2))
print(dict2)
