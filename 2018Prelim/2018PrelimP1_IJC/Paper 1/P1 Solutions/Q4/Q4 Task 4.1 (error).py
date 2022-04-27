###########
# Task 4.1#
###########


#used interchangebly in the code for readability
#[1M - Interpreting '<--']
TEN = 'X'
STRIKE = TEN    

# converting the 'X' or 'number' to int 
#[1M - If Else accuracy]
def Pins(throw):
    if throw == TEN:
        return 10
    else:
        return int(throw)

# recursive solution
#[3M][1M each - interpreting SUM, List, LENGTH]
def Bowling_Score(throws):

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
            frame_score = 10 + Pins(throws[0]) + Pins(throws[1])
            return frame_score + Bowling_Score_Helper(throws[1:], frame_num + 1)

        frame_score = Pins(throws[0]) + Pins(throws[1])

        # spare
        if frame_score == 10:
            return 10 + Pins(throws[2]) + Bowling_Score_Helper(throws[2:], frame_num + 1)

        # frame with no bonus
        return frame_score + Bowling_Score_Helper(throws[2:], frame_num + 1)

    return Bowling_Score_Helper(throws, 1)

##For Evidence 9
print(Bowling_Score('X2815X91X365452X0X'))
print(Bowling_Score('91739182X90X90X82X'))
print(Bowling_Score('91739182X90X90X81'))
print(Bowling_Score('X737291XXX2364733'))
print(Bowling_Score('0580X05X6405819150'))
print(Bowling_Score('XXXX91X002282XXX'))


