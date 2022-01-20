data = [ "Fozzie", 34, \
         "Kermit", 78, \
         "Miss Piggy", 23, \
         "Gonzo", 55, \
         "Beaker", 88, \
         "Honeydew", 59, \
         "Animal", 10, \
         "Rowlf", 54, \
         "Bunsen", 70, \
         "Walter", 51, \
         "Sam Eagle", 19, \
         "Scooter", 62, \
         "Pepe", 45, \
         "Gremlin", 4, \
         "Sweetums", 60, \
         "Hoggart", 39, \
         "Skittle", 49, \
         "Gumbal", 38, \
         "Rizzo", 45, \
         "Bratrat", 14,
         "Mongo", 95]

def result(list):
    i = 0
    while i != len(list):
        if int(list[i+1]) < 40:
            print(list[i].ljust(10), str(list[i+1]).rjust(4), "fail".rjust(10))
        elif int(list[i+ 1]) >= 40 and int(list[i + 1]) < 60:
            print(list[i].ljust(10), str(list[i+1]).rjust(4), "pass".rjust(10))
        elif int(list[i+ 1]) >= 60 and int(list[i + 1]) < 70:
            print(list[i].ljust(10), str(list[i+1]).rjust(4), "merit".rjust(10))
        elif int(list[i+ 1]) >= 70:
            print(list[i].ljust(10), str(list[i+1]).rjust(4),"Distinction".rjust(10))
        else:
            print("Not genuine")
        i = i + 2
d = result(data)
print(d)

print("STUDENTS THAT FAILED AND NEED RESUBMISSION")

def Makeup(list):
    i = 0
    while i != len(list):
        if int(list[i + 1]) >= 30 and int(list[i + 1]) <= 39:
            print(list[i].ljust(10), str(list[i + 1]).rjust(4), "resubmission".rjust(10))
        elif int(list[i + 1]) < 30:
            print(list[i].ljust(10), str(list[i + 1]).rjust(4), "fail".rjust(10))
        i = i + 2
d = Makeup(data)

def studentstat(data):
    highest = 0
    lowest = 100
    highestname = ""
    total = 0

    for k in range(0, len(data), 2):
        score = int(data[k+1])
        name = data[k]
        if score > highest:
            highest = score
            highestname = name
        if score < lowest:
            lowest = score
        total = total + score

        avg = total/(len(data)/2)

    return (highestname, highest, lowest, total, avg)

highestname, highest, lowest, total, avg = studentstat(data)
print(highest, highestname)
print("Mark Range: ", highest, "and", lowest)
print("Total Mark Score: ", total)
print("Average Mark Score: ", avg)

print("STUDENT THAT SCORE ABOVE AVERAGE")
def stat(data):
    total = 0
    countabove = 0
    countbelow = 0
    fail = 0

    for z in range(0, len(data), 2):
        score = data[z+1]
        total = score + total
    average = total/(len(data)/2)
    print("Average is: ", average)

    for x in range(0, len(data), 2):
        if int(data[x+1]) > average:
            countabove = countabove + 1
        elif int(data[x+1]) < average:
            countbelow = countbelow + 1
        if int(data[x+1]) < 40:
            fail = fail + 1

    print("Number of students that score above average :", countabove)
    print("Number of students that score below average :", countbelow)
    print("Number of students that failed :", fail)

stat(data)

