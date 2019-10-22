
soz=[]
s=set('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
while True:
    word=input("soz engiz:")
    if word=='ok':
       break
    soz.append(word)
for i in soz:
    if len(set(soz)-s)!=0:
        soz[i]=soz[i+1]
print(soz)

