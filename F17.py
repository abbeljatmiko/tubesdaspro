from F16 import save

def exit():
    x = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')
    while not (x == "Y" or x == "y") or (x == "n" or x == "N"):
        x = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')

        if (x == "Y") or (x == "y"):
            save()

        elif (x == "N") or (x =="n"):
            break
        else:
            print("Masukan tidak valid")



    # else, tidak di save
