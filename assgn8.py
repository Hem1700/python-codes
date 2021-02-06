fname = input("Enter the file name : ")
count =0
number = 0.0
sum = 0.0
try:
    fhand = open(fname)
except:
    print("File not found.")
    quit()
for letter in fhand:
    if letter .startswith("X-DSPAM-Confidence:"):
        print(letter)
        count = count+1;
        first = letter.find('0')
        print(first)
        last = letter.find('\n')
        print(last)
        digits = print(letter[first:last])
        print(digits)
        sum = float(sum+digits)
        number = number+1
        print(number)
