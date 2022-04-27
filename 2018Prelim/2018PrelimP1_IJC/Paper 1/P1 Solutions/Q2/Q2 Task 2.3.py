##Task 2.3
##Search Hash Table

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

###print contents of hash table
##print('Hash table contents:')
##for i in range(len(hashtable)):
##	print(hashtable[i])

##########
#Task 2.3#
##########
	
#Hash Search Function
def HashSearch(ID):
    #ID not in table
    if int(ID) not in hashtable:
        return 'Student Number not found'

    #ID in table
    HashAddress = int(ID)%12
    if hashtable[HashAddress] == int(ID):
        return HashAddress
    else:
        while hashtable[HashAddress] != int(ID):
            if HashAddress + 1 == 12:
                HashAddress = 0
            else:
                HashAddress += 1
    return HashAddress

#Search Student Number from User Input        
userInput = input('Please enter a student number:')
print(HashSearch(userInput))



