import os


def save():
    def ubahKeString(header, title):
        # Fungsi yang mengubah seluruh data yang ada menjadi string
        global header_user, user
        global header_game, game
        global header_kepemilikan, kepemilikan
        global header_riwayat, riwayat
        if title == user and header == header_user:
            stringuser = ";".join(header_user) + "\n"
            for arr in user:
                stringuser += arr["id"] + ";"
                stringuser += arr["username"] + ";"
                stringuser += arr["nama"] + ";"
                stringuser += arr["password"] + ";"
                stringuser += arr["role"] + ";"
            return stringuser
        elif title == game and header == header_game:
            stringgame = ";".join(header_game) + '\n'
            for arr in game:
                stringgame += arr["id"] + ";"
                stringgame += arr["kategori"] + ";"
                stringgame += arr["tahunrilis"] + ";"
                stringgame += arr["harga"] + ";"
                stringgame += arr["stok"] + ";"
        elif title == kepemilikan and header == header_kepemilikan:
            stringkepemilikan = ";".join(header_kepemilikan) + '\n'
            for arr in kepemilikan:
                stringkepemilikan += arr["game_id"] + ";"
                stringkepemilikan += arr["user_id"] + ";"
        elif title == riwayat and header == header_riwayat:
            stringriwayat = ";".join(header_riwayat) + '\n'
            for arr in riwayat:
                stringriwayat += arr["game_id"] + ";"
                stringriwayat += arr["nama"] + ";"
                stringriwayat += arr["harga"] + ";"
                stringriwayat += arr["user_id"] + ";"
                stringriwayat += arr["tahun_beli"] + ";"

    namafolder = input("Masukkan nama folder penyimpanan: ")
    location = os.path.join(os.path.abspath(os.getcwd()), namafolder)

    try:
        os.makedirs(location)
    except:
        None

    data_sebagai_string_user = ubahKeString(header_user, user)
    data_sebagai_string_game = ubahKeString(header_game, game)
    data_sebagai_string_riwayat = ubahKeString(header_riwayat, riwayat)
    data_sebagai_string_kepemilikan = ubahKeString(header_kepemilikan, kepemilikan)

    file_user = open(os.path.abspath(os.getcwd()) + "\\" + namafolder + "\\" + "user.csv", "w")
    file_user.write(data_sebagai_string_user)

    file_game = open(os.path.abspath(os.getcwd()) + "\\" + namafolder + "\\" + "game.csv", "w")
    file_game.write(data_sebagai_string_game)

    file_riwayat = open(os.path.abspath(os.getcwd()) + "\\" + namafolder + "\\" + "riwayat.csv", "w")
    file_riwayat.write(data_sebagai_string_riwayat)

    file_kepemilikan = open(os.path.abspath(os.getcwd()) + "\\" + namafolder + "\\" + "kepemilikan.csv", "w")
    file_kepemilikan.write(data_sebagai_string_kepemilikan)

    file_user.close()
    file_game.close()
    file_riwayat.close()
    file_kepemilikan.close()

    print("Saving...")
    print("Data telah berhasil disimpan")
