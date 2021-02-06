n= input("Enter a number:")
num = int(n)
if num<=0:

    print("It is neither prime nor composite")
elif num>1:

    for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break

       else:

           print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
