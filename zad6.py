import math
C=50
H=30
d=input('')
D=d.split(',')
print(len(D))
for i in range(0,len(D)):
    Q=math.sqrt((2*C*int(D[i]))/H)
    print(int(Q))