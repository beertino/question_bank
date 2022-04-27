#create hashtable
hashtable = []
for i in range(12):
    hashtable += ['Empty']

#hash function
def hash(key):
    location = int(key)%12
    hashtable[location]=int(key)

#read contents from file
f = open('KEYS.TXT')

keys = []
for line in f:
    keys.append(line.strip())

f.close()

#store contents into hash table
for i in keys:
    hash(i)

#print contents of hash table
print('Hash table contents:')
for i in range(len(hashtable)):
	print(hashtable[i])
