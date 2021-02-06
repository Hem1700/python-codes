text = "X-DSPAM-Confidence:    0.8475";
first = text.find('0')
print(first)
last = text.find('5')
print(last)
digit = float(text[first-1 : last+1])
print(digit)
