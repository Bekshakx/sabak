from fact import fact
n = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = []
k=0
while True:
    count = 0
    x = input("Engiz:")
    for each in x:
        if each in n:
            count += 1
    if len(x) != count:
        if x in ['ok']:
            break
        print("Kayta")
    elif "." in x:
        print("kayta")
    else:
        sum.append(int(x)) 
if len(sum) != 0:
    print(sum)
    for i in range(0,len(sum)):
        k+=int(sum[i])
    print(fact(k))