n=int(input("Enter number:"))
#count=0
sum = 0
#while(n>0):
#    count=count+1
#    n=n//10
#print(count)
temp = n
digit = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
# display the result
if n == sum:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
