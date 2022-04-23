from function import *

def ubah_stok(dfgame):
    id = input("Masukkan id game: ")

    found = False           # Variabel found untuk menentukan apakah ID game sudah ketemu atau belum
    i = 0                   

    while found == False:
        if dfgame[i][0] == id:
            found = True
        
        else:
            i += 1
    
    if found == True:                           # Jika terdapat ID game dalam game.csv
        stok = int(dfgame[i][5])                # Stok terdapat pada kolom ke 4 dalam game.csv
        newStok = input("Masukkan jumlah: ")
        if (newStok > 0):
            stok += newStok
            stok = dfgame[i][5]
            print("Stok game " + dfgame[i][1] + " berhasil ditambahkan. Stok sekarang: " + stok)
    
        elif (newStok < 0):                     # Jika ingin mengurangi stok harus dilihat apakah jumlah yang ingin dikurang menyebabkan stok sekarang menjadi negatif atau tidak
            if stok < (newStok*(-1)):
                print("Stok game " + dfgame[i][1] + " gagal dikurangi karena stok kurang. Stok sekarang: " + stok)
            else:
                stok += newStok
                stok = dfgame[i][5]
                print("Stok game " + dfgame[i][1] + " berhasil dikurangi. Stok sekarang: " + stok)
    else:
        print("Tidak ada game dengan ID tersebut!")