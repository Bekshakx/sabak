from factorial import Bekzhan
sum=[]
a=set("0123456789.")
def A():
    n = set(".0123456789")
    a = []
    while True:
        s = input()
        if len(set(s) - n) != 0:
            if s in ['ok']:
                break
            print("Kayta")
        elif '.' in s:
            print("kayta")
        else:
            sum.append(int(s))
    if len(sum) != 0:
        print(sum)
        print(Bekzhan(sum))
        
    
print(A())



