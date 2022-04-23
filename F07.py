from function import *

def list_game_toko(dfgame) :
    skema=input("Skema sorting : ")
    jenis=skema[:-1]
    keterangan=skema[-1:]
    
    if(jenis=="tahun") :
        if(keterangan=='+') :
            for i in range(1,length(dfgame)) :
                for j in range(i,length(dfgame)) :
                    if(dfgame[i][3] > dfgame[j][3]) :
                        (dfgame[i],dfgame[j]) = (dfgame[j],dfgame[i])
            print_data(dfgame)

        elif(keterangan=='-') :
            for i in range(1,length(dfgame)) :
                for j in range(i,length(dfgame)) :
                    if(dfgame[i][3] < dfgame[j][3]) :
                        (dfgame[i],dfgame[j]) = (dfgame[j],dfgame[i])
            print_data(dfgame)
        else :
            print("Skema sorting tidak valid!")
        
    elif(jenis=="harga") :
        if(keterangan=='+') :
            for i in range(1,length(dfgame)) :
                for j in range(i,length(dfgame)) :
                    if(dfgame[i][4] > dfgame[j][4]) :
                        (dfgame[i],dfgame[j]) = (dfgame[j],dfgame[i])
            print_data(dfgame)
        elif(keterangan=='-') :
            for i in range(1,length(dfgame)) :
                for j in range(i,length(dfgame)) :
                    if(dfgame[i][4] < dfgame[j][4]) :
                        (dfgame[i],dfgame[j]) = (dfgame[j],dfgame[i])
            print_data(dfgame)
        else :
            print("Skema sorting tidak valid!")

    elif(jenis=='') :
        for i in range(1,length(dfgame)) :
                for j in range(i,length(dfgame)) :
                    if(dfgame[i][0] > dfgame[j][0]) :
                        (dfgame[i],dfgame[j]) = (dfgame[j],dfgame[i])
        print_data(dfgame)
    else :
        print("Skema sorting tidak valid!")
    
list_game_toko(get_data("game.csv"))

