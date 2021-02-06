fname = input("Enter the file name : ")
try:
    fhand = open(fname)
except:
    print("File not found.")

for letter in fhand:
    print(letter.upper())
