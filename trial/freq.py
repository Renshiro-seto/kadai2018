import sys
args = sys.argv
f = open(args[1], 'r')

data = f.read()
splits = data.split()

words = {}
for word in splits:
    words[word] = words.get(word, 0) + 1

d = [(v,k)for k,v in words.items()]

d.sort()

for v,k in d [10:]:
    print ("     %d %s" %(v, k))

f.close()

