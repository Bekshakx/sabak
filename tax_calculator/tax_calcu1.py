class Company:
    zhalpy_zhalaky=0
    nalogg=0
    

    def fiz_lico():
        q=[]
        count=0
        mrp=42500
        nalog=[]
        tabys=[]
        zhalaky=input("Жалақыны енгізіңіз: ")
        if ',' in zhalaky:
            a=zhalaky.split(',')
        elif ' ' in zhalaky:
            a=zhalaky.split(' ')
        else:
            a=zhalaky.split(',')
        
        for each in a:
            print(a)
            a1=set(each)
            count=0
            for i in a1:
                count+=1
            if len(a1)==count:
                q.append(each)
       
        for i in range(len(q)):
            print("Кызметкер №:",i+1)
            opv=int(q[i])*0.1
            ipn=(int(q[i])-opv-mrp)*0.1
            so=(int(q[i])-opv)*0.035
            sn=((int(q[i])-opv)*0.095)-so
            med_strh=int(q[i])*0.015
            taza_tabys=int(q[i])-(opv+ipn)
            comp_nalog=so+sn+med_strh
            nalog.append(comp_nalog)
            tabys.append(q[i])
            print("Қызметкер таза жалақысы: {}\nопв={}\nипн={}\ncо={}\nсн={}\nМед.стр={}\nКомпания налогы:{}\n ".format(int(taza_tabys),int(opv),int(ipn),int(so),int(sn),int(med_strh),int(comp_nalog)))
        for i in range(len(tabys)):
            Company.zhalpy_zhalaky+=int(tabys[i])
        for i in range(len(nalog)):
            Company.nalogg+=int(nalog[i])
        
        print("Қызметкерлерге берілетін жалпы жалақы: {}\nКомпания жалпы налогы: {} ".format(Company.zhalpy_zhalaky,Company.nalogg))
    def yur_lico():
        tabys=int(input("Компанияның табысын енгізіңіз: "))
        shygys=int(input("Компанияның шығысын енгізіңіз: "))
        nalog1=tabys*0.03
        nalog2=(tabys-shygys)*0.01
        taza_shygyn=nalog1+nalog2+shygys+Company.zhalpy_zhalaky+Company.nalogg
        taza_tab=tabys-taza_shygyn
        print("\nКомпания шығыны: {}\nЖалпы компания табысы:{}\n ".format(int(taza_shygyn),int(taza_tab)))
    def keri():
        count=0
        f=[]
        c=(input("Таза жалақыны енгізіңіз: "))
        if ',' in c:
            w=c.split(',')
        elif ' ' in c:
            w=c.split(' ')
        else:
            w=c.split(',')
        for each in w:
            w1=set(each)
            count=0
            for i in w1:
                count+=1
            if len(w1)==count:
                f.append(each)
        for i in range(len(f)):
            print("Кызметкер №:",i+1)
            print("Таза жалақы:",f[i])
            d=(100*int(f[i])-425000)/81
            print("Жалпы жалақы:{}".format(int(d)))
        
        

a=Company
a.fiz_lico()
a.yur_lico()
a.keri()

