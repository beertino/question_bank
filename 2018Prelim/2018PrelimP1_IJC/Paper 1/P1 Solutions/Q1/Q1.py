'''
Q1 - 15 marks
Task 1.1
'''

#Read lines from file into DrinkList
f = open('DRINKS.TXT')
Drinklist = []

for line in f:
    Drinklist += [line.strip()]
f.close()

#Menu
print('Menu\n')
print('1. Brewed coffee')
print('2. Brewed tea')
print('3. Other drinks\n')

#Function to return list
def output(lst, selection):
    print(selection+'\n')
    for i in lst:
        print(i)
    print('\nTotal items: ',len(lst))
    
#User input
user_input = input('Option:')

return_list = []

#Menu options

#Option 1
if user_input == '1':
    for i in Drinklist:
        if 'Kopi' in i:
            return_list.append(i)
    output(return_list, "Brewed coffee")

#Option 2
elif user_input == '2':
    for i in Drinklist:
        if 'Teh' in i:
            return_list.append(i)
    output(return_list, "Brewed tea")

#Option 3
elif user_input == '3':
    for i in Drinklist:
        if ('Kopi' not in i) and ('Teh' not in i):
            return_list.append(i)
    output(return_list, "Other drinks")

#Handling invalid input
else:
    print('No such option.')
