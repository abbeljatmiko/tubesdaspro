from function import *

def tambah_game(dfgame):
    nama = input("Masukkan nama game: ")

    def sudahAda(dfgame, nama):
        cek = False                             
        for i in range(length(dfgame)):
            if (dfgame[i][1] == nama):
                cek = True
        return cek

    if (sudahAda(dfgame, nama) == True):
        print("Game", nama, "sudah ada di toko!")

    else:

        kategori = input("Masukkan kategori: ")
        tahun = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok = input("Masukkan stok awal: ")
        
        while (nama == "" or kategori == "" or tahun == "" or harga == "" or stok == ""):
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            nama = input("Masukkan nama game: ")

            if (sudahAda(dfgame, nama)):
                print("Game", nama, "sudah ada di toko!")
            else:

                kategori = input("Masukkan kategori: ")
                tahun = input("Masukkan tahun rilis: ")
                harga = input("Masukkan harga: ")
                stok = input("Masukkan stok awal: ")
        
        if (nama != "" and kategori != "" and tahun != "" and harga != "" and stok != ""):
            print("Selamat! Berhasil menambahkan game", (nama))

        