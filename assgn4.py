sum= 0.0
avg = 0.0
total = 0
while True:
    num=input('Enter a number')
    if num =="Done":
        break
    numb = float(num)
    total = total+1
    sum = sum+ numb
    print(sum)


print('Done!')
print(total)
print(sum)
print(sum/total)
