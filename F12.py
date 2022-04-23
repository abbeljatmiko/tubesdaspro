from function import *

def topup(dfuser):
    
    username = input("Masukkan username: ")
    try:                                                            
        saldo = float(input("Masukkan saldo: "))
        
        check = False                                           # Inisialisasi validasi user
        for i in range(1, length(dfuser)):                   
            if username == (dfuser[i][1]):                      # User tervalidasi
                saldoakhir = float(dfuser[i][5])                  # data saldo user diubah menjadi integer
                saldoakhir += saldo                             # operasi penambahan/pengurangan saldo
                if saldoakhir < 0:                              # saldo berupa negatif
                    print("Masukan tidak valid")
                else:
                    dfuser[i][5] = str(saldoakhir)              # saldoakhir diubah lagi menjadi string
                    if (saldo >= 0):
                        print("Top up berhasil. Saldo", dfuser[i][2],"bertambah menjadi "+str(saldoakhir)+".")       # Bila ditambahkan
                    else :
                        print("Top up berhasil. Saldo", dfuser[i][2],"berkurang menjadi "+str(saldoakhir)+".")       # Bila dikurangi
                check = True                                    # Nama user tersedia di user.csv
                break                                           # ketika sudah selesai maka loop dihentikan

        if not check:                                           # user tidak tersedia di user.csv
            print("Username '"+username+"' tidak ditemukan.")
    except :
        print("Input tersebut tidak diterima.")
    return dfuser