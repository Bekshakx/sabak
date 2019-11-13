class Nalog:
    mem=0
    y=0
    nall1=0
    def __init__(self):
        numbers=['.','0','1','2','3','4','5','6','7','8','9']
        sum2=0
        s=[]
        tabis=[]
        mzp=42500
        nall=[]
        y=input("Жалақыны енгізіңіз: ")
        a=y.split(',')
        for each in a:
            set_split=set(each)
            sum2=0
            for i in set_split:
                sum2+=1
            if len(set_split)==sum2:
                s.append(each)             
        print(s)