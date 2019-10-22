students = {}
name = []
sum=0
while True:
    aty = input("atyndy engiz: \n")
    if aty == "stop":
        break
    ball = int(input("ball engiz: \n"))
    students[aty]=ball
print(students)

for i in range(len(students)):
    sum+=list(students.items())[i][1]
sum1=sum/len(students)
print(" Ortasha ball: {}".format(sum1))
for i in range(len(students)):
    if list(students.items())[i][1]<sum1:
        name.append(list(students.items())[i][0])
print(" Ortashadan tomen ball algan student: {}".format(name))