fname  = input("Enter file name : ")
fhandle = open(fname)
lst = list()
for line in fhandle:
    final = line.split()
    for element in final:
        if element in lst:
            continue
        else :
            lst.append(element)
lst.sort()
print(lst)
