str = input("Enter a string:")
reversed_string = reversed(str)
print(reversed_string)
rev = ''.join(reversed_string)
print(rev)
if (str==rev):
    print("It is an palindrome")
else:
    print("It is not ")
