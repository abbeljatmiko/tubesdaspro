def search_game_at_store(datagame):
    filtersearch = ["","","","",""]
    filtersearch[0] = (input("Masukkan ID: "))
    filtersearch[1] = (input("Masukkan Nama Game: "))
    filtersearch[4] = (input("Masukkan Harga Game: "))
    filtersearch[2] = (input("Masukkan Kategori Game: "))
    filtersearch[3] = (input("Masukkan Tahun Rilis Game: "))

    nomer = 1
    print("Daftar game pada toko yang memenuhi kriteria: ")
    for indeks in datagame:

        if indeks[0] != "id" :
            sesuai = True
            for i in range(5):
                if filtersearch[i] != "" and filtersearch[i] != indeks[i]:
                    sesuai = False
            if sesuai:
                print(f"{nomer}. {indeks[0]:5s} | {indeks[1]:20s} | {indeks[4]:7s} | {indeks[2]:10s} | {indeks[3]:4s} | {indeks[5]:1s} ")
                nomer += 1
    if nomer == 0:
        print("Tidak ada")
