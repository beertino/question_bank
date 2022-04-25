#################
# Task 4.2 + 4.3#
#################

'''
Test Cases
1. Boundary test case: '00000000000000000000'
2. Boundary test case: 'XXXXXXXXXXXX'
3. Invalid characters: 'XxXXXXXXXXXY'
'''

#used interchangebly in the code for readability
#[1M - Interpreting '<--']
TEN = 'X'
STRIKE = TEN    

# converting the 'X' or 'number' to int 
#[1M - If Else accuracy]
def Pins(throw):    
    return 10 if throw == TEN else int(throw)

# recursive solution
#[3M][1M each - interpreting SUM, List, LENGTH]
def Bowling_Score(throws):

    ##Test for Invalid Characters
    charlist = ['0','1','2','3','4','5','6','7','8','9','X']
    for i in throws:
        if i not in charlist:
            return 'Invalid Characters.'

    # need a helper function to keep track of the current frame number
    def Bowling_Score_Helper(throws, frame_num):

        # account for frame 10 first
        # last frame with no bonus
        if frame_num == 10 and len(throws) == 2:
            return Pins(throws[0]) + Pins(throws[1])

        # if the last frame contains 3 throws, then it must be a spare or strike
        # In both cases, the score is computed in the same way.
        if frame_num == 10 and len(throws) == 3:
            return Pins(throws[0]) + Pins(throws[1]) + Pins(throws[2])

        # strike
        if throws[0] == STRIKE:
            frame_score = 10 + Pins(throws[1]) + Pins(throws[2])
            return frame_score + Bowling_Score_Helper(throws[1:], frame_num + 1)

        frame_score = Pins(throws[0]) + Pins(throws[1])

        # spare
        if frame_score == 10:
            return 10 + Pins(throws[2]) + Bowling_Score_Helper(throws[2:], frame_num + 1)

        # frame with no bonus
        return frame_score + Bowling_Score_Helper(throws[2:], frame_num + 1)

    return Bowling_Score_Helper(throws, 1)

'''
Task 4.3
'''

def total_score(lst):
    total = 0
    scores = lst[2:]
    #print(scores)
    for score in scores:
        #print(score)
        #print(Bowling_Score(score))
        total += Bowling_Score(score)
    return total

f = open('SCORES.TXT')
lst = []
for row in f:
    lst += [row.split()]
    #print(lst)
f.close()

scorelst = []
for entry in lst:
    #print(entry)
    scorelst += [[entry[0],entry[1],total_score(entry)]]

##Bubble Sort (decending) Function Here##
def bubble_sort(lst):
    if len(lst) < 2:
        return
    for j in range(len(lst)-1):
        for i in range(len(lst)-1-j):
            if lst[i][2]<lst[i+1][2]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

bubble_sort(scorelst)
print(scorelst)

'''
Output of Results
'''

print('Official Results\n')
print('{0:8}{1:^20}{2:^10}{3:^11}'.format('Position','Register Number','Country','Total Score'))
rank = 0 #to print position
for i in scorelst:
    print('{0:^8}{1:^20}{2:^10}{3:^11}'.format(rank+1,i[0],i[1],i[2]))
    rank += 1
