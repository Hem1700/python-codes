fname = input("Enter file name : ")
handle  = open(fname)
bigword = None
bigcount = None
counts = dict()
for lines in handle:
    if not lines.startswith('From '): continue
    words = lines.split()
    counts[words[1]]=counts.get(words[1],0)+1
for word,count in counts.items():
    if bigword is None or count>bigcount:
        bigword = word
        bigcount=count
print(bigword , bigcount)
