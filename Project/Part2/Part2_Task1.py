GET name user
IF name empty or space SET name="Anonymous gamer"

SET random GOAL from range 1 to 100
SET random DICE from range 1 to 6

DISPLAY greeting, game conditions and number of attempts

START for loop iterating by DICE

GET NUMBER from user

IF NUMBER is out of range
BREAK the cycle
DISPLAY loser message

IF NUMBER equals GOAL
BREAK the cycle
DISPLAY winner message

IF NUMBER is less than GOAL
DISPLAY comparison result
DISPLAY remaining attempts
     IF remaining attempts = 0
     DISPLAY loser message
     SET WIN = False

IF NUMBER is more than GOAL
DISPLAY comparison result
DISPLAY remaining attempts
     IF remaining attempts = 0
     DISPLAY loser message
     SET WIN = False

IF WIN is True SET RESULT = WIN
ELSE SET RESULT = LOSE

START STATISTICS BLOCK

CREATE or APPEND the Statistics document with the current game results
in format
result | attempts | name
SAVE and CLOSE the file

OPEN file in READ mode
DISPLAY all statistics
CLOSE the file