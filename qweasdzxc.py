from fact import fact
sum=[]
k=0
n=set(".0123456789")
while True:
    s=input("engiz:")
    if len(set(s)-n)!=0:
        if s in ['ok']:
            break
        print("kayta")
    elif '.' in s:
        print("kayta")
    else:
        sum.append(int(s))
if len(sum)!=0:
    print(sum)
    for i in range(len(sum)):
        k+=int(sum[i])
    print(k)
    print(fact(k))
else:
    pass
    