from function import *

def list_game_toko(dfgame) :
    skema=input("Skema sorting : ")
    jenis=skema[:-1]
    keterangan=skema[-1:]
    list=dfgame
    len=length(dfgame)
    
    if(jenis=="tahun") :
        if(keterangan=='+') :
            for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][3]>list[j][3]) :
                        (list[i],list[j])=(list[j],list[i])
            print_data(list)

        elif(keterangan=='-') :
            for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][3]<list[j][3]) :
                        (list[i],list[j])=(list[j],list[i])
            print_data(list)
        else :
            print("Skema sorting tidak valid!")
        
    elif(jenis=="harga") :
        if(keterangan=='+') :
            for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][4]>list[j][4]) :
                        (list[i],list[j])=(list[j],list[i])
            print_data(list)
        elif(keterangan=='-') :
            for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][4]<list[j][4]) :
                        (list[i],list[j])=(list[j],list[i])
            print_data(list)
        else :
            print("Skema sorting tidak valid!")

    elif(jenis=='') :
        for i in range(1,len) :
                for j in range(i,len) :
                    if(list[i][0]>list[j][0]) :
                        (list[i],list[j])=(list[j],list[i])
        print_data(list)
    else :
        print("Skema sorting tidak valid!")
    
list_game_toko(get_data("game.csv"))

