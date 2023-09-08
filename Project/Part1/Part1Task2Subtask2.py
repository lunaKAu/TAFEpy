confPack = open("confPack.txt", "r")
people = open("employees.txt", "r")
employeesPacks = open("employeesPacks.txt", "w")

pack   = confPack.read()
basic  = pack.split("\n")[0]
bonus  = pack.split("\n")[1]

from datetime import date
dataReport = date.today()
employeesPacks.write("Report date: "+ str(dataReport.day) +"/"+ str(dataReport.month) +"/"+ str(dataReport.year) +"\n\n")

for line in people:
    #remove newline character
    line = line.rstrip()
    name   = line.split(",")[0]
    family = line.split(",")[1]
    day1   = line.split(",")[2]
    day2   = line.split(",")[3]

    employeesPacks.write("Attendee: " + name + " " + family + "\n")

    if  (day1 == "Y" and day2=="Y"):
        employeesPacks.write("Packs: " + basic + ", ")
        employeesPacks.write(bonus + "\n\n")
    elif (day1 == "Y" or day2 == "Y"):
        employeesPacks.write("Pack: " + basic + "\n\n")
    else:
        employeesPacks.write("\n")

employeesPacks.close()
people.close()
confPack.close()

