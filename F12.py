from function import *


def topup(dfuser):
    username = input("Masukkan username: ")
    try:
        saldo = int(input("Masukkan saldo: "))  # Kondisikan bahwa saldo dalam bentuk bilangan bulat bukan riil
        cek = False

        for i in range(1, length(dfuser)):
            if username == (dfuser[i][1]):  # Cek apakah username terdapat dalam user.csv
                newSaldo = int(dfuser[i][5])
                newSaldo += saldo
                if newSaldo < 0:
                    print("Masukan tidak valid")
                else:
                    dfuser[i][5] = str(newSaldo)
                    if (saldo >= 0):
                        print("Top up berhasil. Saldo", dfuser[i][2], "bertambah menjadi " + str(newSaldo) + ".")
                    else:
                        print("Top up berhasil. Saldo", dfuser[i][2], "berkurang menjadi " + str(newSaldo) + ".")
                cek = True
                break

        if not cek:
            print("Username " + username + " tidak ditemukan.")
    except:
        print("Input tersebut tidak diterima.")
    return dfuser
