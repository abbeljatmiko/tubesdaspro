from function import *



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

    return datauser, kepemilikan, riwayat, datagame


def cek_punya(kepemilikan, userid, gameid):
    for data in kepemilikan:
        if data[0] == gameid:
            if data[1] == userid:
                return True
    return False
