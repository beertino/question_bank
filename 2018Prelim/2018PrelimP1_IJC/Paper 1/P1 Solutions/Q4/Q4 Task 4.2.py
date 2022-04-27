############
# Task 4.2 #
############

'''
Test Cases
1. Boundary test case: '00000000000000000000'
2. Boundary test case: 'XXXXXXXXXXXX'
3. Invalid characters: 'XxXXXXXXXXXY'
'''

#used interchangebly in the code for readability
TEN = 'X'
STRIKE = TEN    

# converting the 'X' or 'number' to int 
def Pins(throw):    
    return 10 if throw == TEN else int(throw)

# recursive solution
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

##Test Cases
print("'00000000000000000000':", Bowling_Score('00000000000000000000'))
print("'XXXXXXXXXXXX':",Bowling_Score('XXXXXXXXXXXX'))
print("'XxXXXXXXXXXY':",Bowling_Score('XxXXXXXXXXXY'))
