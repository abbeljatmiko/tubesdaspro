from function import *

def list_game(data) :
    skema=input("Skema sorting : ")
    jenis=skema[:-1]
    keterangan=skema[-1:]
    list=data
    len=length(data)
    
    if(jenis=="tahun") :
        if(keterangan=='+') :
            for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][3]>list[j][3]) :
                        (list[i],list[j])=swap(list[i],list[j])
            print_data(list)
        elif(keterangan=='-') :
            for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][3]<list[j][3]) :
                        (list[i],list[j])=swap(list[i],list[j])
            print_data(list)
        else :
            print("Skea sorting tidak valid")
        
    elif(jenis=="harga") :
        if(keterangan=='+') :
            for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][4]>list[j][4]) :
                        (list[i],list[j])=swap(list[i],list[j])
            print_data(list)
        elif(keterangan=='-') :
            for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][4]<list[j][4]) :
                        (list[i],list[j])=swap(list[i],list[j])
            print_data(list)
        else :
            print("Skea sorting tidak valid")
    elif(jenis=='') :
        for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][0]>list[j][0]) :
                        (list[i],list[j])=swap(list[i],list[j])
        print_data(list)
    else :
        print("Skema sorting tidak valid!")
list_game(get_data("game.csv"))

