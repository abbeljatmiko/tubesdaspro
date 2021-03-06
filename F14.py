def help(role):
    print("============ HELP ============")
    if role == "Admin":  # role sebagai admin
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. tambah_game - Untuk menambah game yang dijual pada toko")
        print("4. ubah_game - Untuk mengubah game pada toko game")
        print("5. ubah_stok - Untuk mengubah stok game di toko")
        print("6. list_game_toko - Untuk listing game di Toko Berdasarkan ID, Tahun Rilis, dan Harga")
        print(
            "7. search_game_at_store - Untuk mencari game di Toko dari ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
        print("8. topup - Untuk top up saldo")
        print("9. help - Untuk memberikan panduan penggunaan sistem")
        print("10. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")


    elif role == "User":  # jika role sebagai user
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. list_game_toko - Untuk listing game di Toko Berdasarkan ID, Tahun Rilis, dan Harga")
        print("3. buy_game - Untuk membeli game")
        print("4. list_game - Untuk melihat game yang dimiliki")
        print("5. search_my_game - Untuk mencari game yang dimiliki dari ID dan tahun rilis")
        print(
            "6. search_game_at_store - Untuk mencari game di Toko dari ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
        print("7. help - Untuk memberikan panduan penggunaan sistem")
        print("8. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
