from B02 import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F08 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *
from F13 import *
from F14 import *
from F15 import *
from F16 import *
from F17 import *
from function import *
import argparse
import os

# Inisialisasi parser
parser = argparse.ArgumentParser(description='')

# Parameter positional/optional
parser.add_argument("folder")

# parse argument
args = parser.parse_args()

f = str(os.path.abspath(os.getcwd())) + "\\" + str(args.folder)

if args.folder:
    print("Loading...")
    print("Selamat datang di antarmuka Binomo")
else:
    print("Tidak ada nama folder yang diberikan")

dfuser = csv_to_array(f+"\\user.csv")
dfgame = csv_to_array(f+"\\game.csv")
dfriwayat = csv_to_array(f+"\\riwayat.csv")
dfkepemilikan = csv_to_array(f+"\\kepemilikan.csv")

end = False
iduser = 0
command = input(">>>").lower()
while end == False:
    role = "TidakAda"
    log = False


    if command == "login":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        found = False  # Variabel found digunakan untuk menentukan apakah username ketemu pada user.csv
        i = 0

        while found == False:
            if dfuser[i][1] == username and dfuser[i][3] == password:  # Jika sudah ketemu maka variabel found akan menjadi True sehingga loop berhenti
                found = True
                iduser = i
                role = "user"
                print("Login berhasil!")

            else:
                i += 1  # Jika belum ketemu maka akan dilanjutkan pencarian ke row selanjut nya pada kolom username

            if i == (length(dfuser) - 1) and found == False:
                print("Password atau username salah atau tidak ditemukan.")


    if command == "register":
        dfuser = register(dfuser)
    elif command == "tambah_game":
        tambah_game(dfgame)
    elif command == "ubah_game":
        dfgame = ubah_game(dfgame)
    elif command == "ubah_stok":
        dfgame = ubah_stok(dfgame)
    elif command == "list_game_toko":
        list_game_toko(dfgame)
    elif command == "buy_game":
        dfuser,dfkepemilikan,dfriwayat,dfgame = buy_game(iduser,dfkepemilikan,dfgame,dfriwayat,dfuser)
    elif command == "list_game":
        list_game(iduser,dfkepemilikan,dfgame)
    elif command == "search_my_game":
        search_my_game(str(iduser),dfkepemilikan,dfgame)
    elif command == "search_game_at_store":
        search_game_at_store(dfgame)
    elif command == "topup":
        dfuser = topup(dfuser)
    elif command == "riwayat":
        riwayat(str(iduser),dfriwayat)
    elif command == "help":
        help(dfuser[iduser][4])
    elif command =="save":
        save()
    elif command == "exit":
        exit()
    elif command == "kerangajaib":
        kerangajaib()

    else:
        print("Perintah tidak valid, masukkan perintah yang valid atau ketik 'help' ")

    command = input(">>>").lower()
