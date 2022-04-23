from kerangajaib import kerangajaib
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

import argparse
import os 


#Inisialisasi parser
parser = argparse.ArgumentParser(description = '')

#Parameter positional/optional
parser.add_argument("folder")

#parse argument
args = parser.parse_args()

f = str(os.path.abspath(os.getcwd())) + "\\" + str(args.folder)

if args.folder :
    print("Loading...")
    print("Selamat datang di antarmuka Binomo")
else :
    print("Tidak ada nama folder yang diberikan")

fileuser = open(str(f) + "\\" + "user.csv","r")
bacafileuser = fileuser.readlines()
fileuser.close()

filegame = open(str(f) + "\\" + "game.csv","r")
bacafilegame = fileuser.readlines()
filegame.close()

fileriwayat = open(str(f) + "\\" + "riwayat.csv","r")
bacafileriwayat = fileriwayat.readlines()
fileriwayat.close()

filekepemilikan = open(str(f) + "\\" + "kepemilikan.csv","r")
bacafilekepemilikan = filekepemilikan.readlines()
filekepemilikan.close()



end = False

while end == False:
    command = input(">>>").lower()
    log = False
    admin = False
    if command == "login":
        print("====")
    elif command == "tambah_game":
        tambah_game()
    elif command == "ubah_game":
        ubah_game()
    elif command == "ubah_stok":
        ubah_stok()
    elif command == "list_game_toko":
        list_game_toko()
    elif command == "buy_game":
        buy_game()
    elif command == "list_game":
        list_game()
    elif command == "search_my_game":
        search_my_game()
    elif command == "search_game_at_store":
        search_game_at_store()
    elif command == "topup":
        topup()
    elif command == "riwayat":
        riwayat()
    elif command == "help":
        help()
    elif command == "save":
        save()
    elif command == "exit":
        exit()
    elif command == "kerangajaib":
        kerangajaib()

    
