name = input("How can I call you? ")
#Empty name check
if name == "" or name == " ":
    name = "Anonymous gamer"

from random import randint
x = randint(1, 100)
#print("Goal is "+str(x))
dice = randint(1, 6)
print(name + ", I hope you can guess the number from 1 to 100.")
if dice == 1:
    print("You have 1 try!")
else:
    print("You have", dice, "tries.")
#dive+1 allows to include the upper border
for i in range(1, dice + 1):

    usersNumber = int(input("And you think it is: "))

    #Out of range check
    if usersNumber < 1 or usersNumber > 100:
        win = False
        print("Sorry, you misunderstood the task. Next time try to name a number from 1 to 100.")
        break
    elif usersNumber == x:
        win = True
        print("Yohooo! You are the winner!!")
        break
    elif usersNumber < x:
        #attempts left = current dice roll - current iteration number
        print("The entered number is less than the number. Attempts that you have left:", dice - i)
        #no more tries left
        if dice - i == 0:
            print("In the final, you did not guess. I believe that next time luck will be with you.")
            win = False
    else:
        print("The entered number is more than the number. Attempts that you have left:", dice - i)
        if dice - i == 0:
            print("In the final, you did not guess. I believe that next time luck will be with you.")
            win = False

if win:
    win = "Win"
else:
    win = "Lose"

#Statistics block
print("Statistics of other players")

stat = open("Statistics.txt", "a")
stat.write(win + " | " + str(dice) + " | " + name + "\n")
stat.close()

stat = open("Statistics.txt", "r")
statistics = stat.read()
print(statistics)
stat.close()