name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hcount = dict()
hlst = []

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        hr = words[5].split(':')
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1
    else:
        continue

for k,v in hcount.items():
    hlst.append((k,v))
hlst.sort()
for k,v in hlst:
