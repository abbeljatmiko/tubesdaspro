from function import *
a = input(">>>")

data_kepemilikan = csv_to_array(r"C:\Users\indra\PycharmProjects\noobman\tubes\kepemilikan.csv")
data_game = csv_to_array(r"C:\Users\indra\PycharmProjects\noobman\tubes\game.csv")
data_user = csv_to_array(r"C:\Users\indra\PycharmProjects\noobman\tubes\user.csv")
data_riwayat = csv_to_array(r"C:\Users\indra\PycharmProjects\noobman\tubes\riwayat.csv")


def buy_game(userid, kepemilikan, datagame, riwayat, datauser ):


    inp_id = input("Masukkan ID Game : ")   
    saldo_awal = int(datauser[userid][-1])
    index_game = get_index(inp_id)

    if inp_id < datagame[1][0] or inp_id > datagame[-1][0]:
        print("ID tidak ditemukan")

    elif saldo_awal < int(datagame[index_game][-2]):
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")

    elif datagame[index_game][-1] < "1":
        print("Stok Game tersebut sedang habis!")

    elif cek_punya(kepemilikan, str(userid), inp_id):
        print("Anda sudah memiliki Game tersebut!")

    else:
        saldo_akhir = str(saldo_awal - int(datagame[index_game][-2]))
        datauser[userid][-1] = saldo_akhir

        data_punya = [inp_id, userid]
        kepemilikan += [data_punya]

        nama_game = datagame[index_game][1]
        tahun_beli = "2022"
        data_riwayat = [inp_id, nama_game, datagame[index_game][-2], userid, tahun_beli]
        riwayat += [data_riwayat]

        print(f'Game "{nama_game}" telah berhasil dibeli!')

    return datauser, kepemilikan, riwayat


def cek_punya(kepemilikan, userid, gameid):
    for data in kepemilikan:
        if data[0] == gameid:
            if data[1] == userid:
                return True
    return False

user_id = 2
if a == "buy_game":
    data_temp = buy_game(user_id, data_kepemilikan, data_game, data_riwayat, data_user)
    data_user = data_temp[0]
    data_kepemilikan = data_temp[1]
    data_riwayat = data_temp[2]
    print(">>>")