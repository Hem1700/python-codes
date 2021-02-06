l = []
for i in range(1,101):
    if(i%3==0 and i%5==0):
        l.append('BuzzFizz')
        continue

    if(i%3==0):
        l.append('fizz')
        continue
    if (i%5==0):
        l.append('Buzz')
        continue

    else:
        l.append(i)
print(l)        
