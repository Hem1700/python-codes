
fname  = input("Enter File name : ")
fhandle = open(fname)
for line in fhandle:
    if line.startswith("From"):
        flst = line.split()
        print(flst[1])
#        first = line.find('From')
#        last  =
#        print(first)
#        print(line)
