n  = input("Enter a number:")

num = int(n)
factorial = 1
for i in range(1,num+1):
    print(i)
    factorial = factorial*i
print(factorial)
