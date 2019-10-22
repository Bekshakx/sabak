a=2000
result=""
sum=0
while a<=3200:
    if a%7==0 and a%5!=0:
        result=result+str(a)+","
        sum+=1
    a+=1
print(sum)
print(result)