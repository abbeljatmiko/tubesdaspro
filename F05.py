from function import *

def ubah_game(datagame):

    #menginput data game yang akan diubah
    idgame = input("Masukkan ID game:")
    namagame = str(input("Masukkan nama game:"))
    kategori = str(input("Masukkan kategori game: "))
    tahunrilis = input("Masukkan tahun rilis game: ")
    hargagame = input("Masukkan harga game: ")

    #mengassign variabel id game untuk mendapatkan indeks
    idgame = get_index(idgame)

    #deklarasi array isidata untuk diolah lebih lanjut
    isidata = [idgame, namagame , kategori , tahunrilis , hargagame]


    if idgame < 1 or idgame > get_index(datagame[-1][0]):
        print("ID tidak dapat ditemukan!")

    for i in range(4):
        if isidata[i]:
            datagame[idgame][i+1] = isidata[i]

    return datagame

data_game = csv_to_array(r"C:\Users\indra\PycharmProjects\noobman\tubes\game.csv")

print(data_game)
print(ubah_game(data_game))