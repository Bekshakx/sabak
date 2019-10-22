numbers = []
sum=0

for each in range(2000,3201):
    if each%7==0 and each%5!=0:
        numbers.append(each)

        sum+=1
s=""
for each in range(len(numbers)-1):
    s+=str(numbers[each])+","
print(sum)

print(s+str(numbers[-1]))

