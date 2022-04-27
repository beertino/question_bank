##Task 2.2
##Handles Collision

#create hashtable
hashtable = []
for i in range(12):
    hashtable += ['Empty']

#improved hash function
def improvedhash(key):
    BaseAddress = int(key)%12
    while hashtable[BaseAddress] is not 'Empty':
        if BaseAddress + 1 == 12:
                BaseAddress = 0
        else:
                BaseAddress += 1
    hashtable[BaseAddress]=int(key)

#read contents from file KEYS2.TXT
f = open('KEYS2.TXT')

keys = []
for line in f:
    keys.append(line.strip())

f.close()

#store contents into hash table
for i in keys:
    improvedhash(i)

#print contents of hash table
print('Hash table contents:')
for i in range(len(hashtable)):
	print(hashtable[i])
