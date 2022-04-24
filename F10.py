from function import *


def search_my_game(loggeduser,kepemilikan,game):
    gameid = input('Masukkan ID Game: ')
    thrilis = input('Masukkan Tahun Rilis Game: ')
    print('Daftar game pada inventory yang memenuhi kriteria: ')
    ada = False
    c = 0  # Penomoran setiap game yang sesuai
    ii = 0  # Indeks total inventory
    ix = 0  # Indeks pada Inventory
    idx = 0  # Jumlah line data pada file game.csv
    idx1 = 0  # Menghitung jumlah baris pada file kepemilikan.csv
    exist = False  # Menentukan game ada dalam kepemilikan dan sesuai akun (Inisialisasi False)
    sesuaigame = ""
    sesuaiuser = ""
    cc = 0
    bb = 0
    for k in kepemilikan:
        idx1 += 1
    line1 = idx1  # Jumlah baris pada file kepemilikan.csv
    for i in game:
        idx += 1
    line = idx  # Jumlah baris pada file game.csv
    idx = 0  # Reset jumlah

    for x in range(1, line1):
        if (loggeduser + '\n' == kepemilikan[x][1]) or (loggeduser == kepemilikan[x][1]):
            ii += 1
    inventory = ['' for m in range(ii)]
    for z in range(1, line1):  # Pencarian game dalam Inventory
        # print(a)
        # print(a[0], a[1])
        if (gameid == kepemilikan[z][0]) and ((loggeduser == kepemilikan[z][1]) or (loggeduser + '\n' == kepemilikan[z][1])):
            sesuaigame = kepemilikan[z][0]
            inventory[ix] = kepemilikan[z][0]
            if ix < ii - 1:
                ix += 1
            cc = z  # Indeks pada pengecekan kepemilikan sesuai gameid
        if (gameid == '') and ((loggeduser == kepemilikan[z][1]) or (loggeduser + '\n' == kepemilikan[z][1])):
            sesuaigame = 'semua'
            cc = z
            inventory[ix] = kepemilikan[z][0]
            if ix < ii - 1:
                ix += 1
    for z in range(1, line1):  # Klarifikasi keberadaan game dan kesesuaian user
        if (loggeduser == kepemilikan[z][1]) or (loggeduser + '\n' == kepemilikan[z][1]):
            sesuaiuser = loggeduser
            bb = z  # Indeks pada pengecekan kepemilikan sesuai userid
        if ((sesuaigame != '') or (gameid == '')) and (sesuaiuser != '') and (cc == bb):
            exist = True
        if (sesuaigame == 'semua'):
            exist = True
    for j in range(1, line):  # pemrosesan printing game jika ada
        # print(j)
        # a = game[j]
        # print(b)
        for s in game[j]:
            if (gameid == '') and (thrilis == '') and (exist == True):
                for y in inventory:
                    if (y == s):
                        c += 1
                        print(f'{c}.', end=" ")
                        ada = True
                        for o in range(5):
                            if o < 4:
                                print(game[j][o], ' |', end=' ')
                            else:
                                print(game[j][o], end='\n')
            elif (gameid == '') and (thrilis + '\n' == game[j][4] or thrilis == game[j][4]) and (exist == True):
                for y in inventory:
                    if (y == s):
                        c += 1
                        print(f'{c}.', end=" ")
                        ada = True
                        for o in range(5):
                            if o < 4:
                                print(game[j][o], ' |', end=' ')
                            else:
                                print(game[j][o], end='\n')
            elif (gameid == s) and (sesuaigame == gameid) and (thrilis != '') and (exist == True) and (
                    sesuaiuser == loggeduser):  # Input berupa game ID & tahun
                for x in game[j]:
                    if (thrilis == x) or (thrilis + '\n' == x):
                        c += 1
                        print(c, '.', end=' ')
                        ada = True
                        for o in range(5):
                            if o < 4:
                                print(game[j][o], ' |', end=' ')
                            else:
                                print(game[j][o], end='\n')
            elif (gameid == s) and (sesuaigame == gameid) and (thrilis == '') and (exist == True) and (
                    sesuaiuser == loggeduser):  # Input berupa hanya game ID
                for y in inventory:
                    if (y == gameid) or (y == gameid + '\n'):
                        c += 1
                        print(f'{c}.', end=' ')
                        ada = True
                        for o in range(5):
                            if o < 4:
                                print(game[j][o], ' |', end=' ')
                            else:
                                print(game[j][o], end='\n')
    if (ada != True):
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
