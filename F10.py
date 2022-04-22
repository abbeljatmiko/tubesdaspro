from function import *

def search_my_game(loggeduser):
    gameid = input('Masukkan ID Game: ')
    thrilis = input('Masukkan Tahun Rilis Game: ')
    print('Daftar game pada inventory yang memenuhi kriteria: ')
    fx = list(open('game.csv', 'r'))
    f = list(open('kepemilikan.csv', 'r'))
    ada = False
    c = 0 # Penomoran setiap game yang sesuai
    ii = 0 # Indeks total inventory
    ix = 0 # Indeks pada Inventory
    idx = 0 # Jumlah line data pada file game.csv
    idx1 = 0 # Menghitung jumlah baris pada file kepemilikan.csv
    exist = False # Menentukan game ada dalam kepemilikan dan sesuai akun (Inisialisasi False)
    for k in f:
        idx1 +=1
    line1 = idx1 # Jumlah baris pada file kepemilikan.csv
    for i in fx:
        idx +=1
    line = idx # Jumlah baris pada file game.csv
    idx = 0 # Reset jumlah

    for x in range(1, line1):
        a = splitFunction(f[x])
        if (loggeduser+'\n' == a[1]) or (loggeduser == a[1]):
            ii += 1
    inventory = ['' for m in range(ii)]
    for z in range(1, line1): # Pencarian game dalam Inventory
        a = splitFunction(f[z])
       # print(a)
       # print(a[0], a[1])
        if (gameid == a[0]) and ((loggeduser == a[1]) or (loggeduser+'\n' == a[1])):
            sesuaigame = a[0]
            inventory[ix] = a[0]
            if ix < ii-1:
                ix +=1
            cc = z # Indeks pada pengecekan kepemilikan sesuai gameid
        if (gameid == '') and ((loggeduser == a[1]) or (loggeduser+'\n' == a[1])):
            sesuaigame = 'semua'
            cc = z
            inventory[ix] = a[0]
            if ix < ii-1:
                ix +=1
    for z in range(1, line1): # Klarifikasi keberadaan game dan kesesuaian user
        a = splitFunction(f[z])
        if (loggeduser == a[1]) or (loggeduser+'\n' == a[1]):
            sesuaiuser = loggeduser
            bb = z # Indeks pada pengecekan kepemilikan sesuai userid
        if ((sesuaigame != '') or (gameid == '')) and (sesuaiuser != '') and (cc == bb):
            exist = True
        if (sesuaigame == 'semua'):
            exist = True
    for j in range(1, line): # pemrosesan printing game jika ada
        #print(j)
       # a = fx[j]
        b = splitFunc(fx[j])
        #print(b)
        for s in b:
            if (gameid == '') and (thrilis == '') and (exist == True):
                for y in inventory:
                    if (y == s):
                        c+=1
                        print(f'{c}.',end=" ")
                        ada = True
                        for o in range(5):
                            if o < 4:
                                print(b[o],' |', end=' ')
                            else:
                                print(b[o], end='\n')
            elif (gameid == '') and (thrilis+'\n' == b[4] or thrilis == b[4]) and (exist == True):
                for y in inventory:
                    if (y == s):
                        c+=1
                        print(f'{c}.',end=" ")
                        ada = True
                        for o in range(5):
                            if o < 4:
                                print(b[o],' |', end=' ')
                            else:
                                print(b[o], end='\n')
            elif (gameid == s) and (sesuaigame == gameid) and (thrilis != '') and (exist == True) and (sesuaiuser == loggeduser): # Input berupa game ID & tahun
                for x in b:
                    if (thrilis == x) or (thrilis+'\n' == x):
                        c+=1
                        print(c,'.',end=' ')
                        ada = True
                        for o in range(5):
                            if o < 4:
                                print(b[o],' |', end=' ')
                            else:
                              print(b[o], end='\n')
            elif (gameid == s) and (sesuaigame == gameid) and (thrilis == '') and (exist == True) and (sesuaiuser == loggeduser): # Input berupa hanya game ID
                for y in inventory:
                    if (y == gameid) or (y == gameid+'\n'):
                        c+=1
                        print(f'{c}.',end=' ')
                        ada = True
                        for o in range(5):
                            if o < 4:
                                print(b[o],' |', end=' ')
                            else:
                                print(b[o], end='\n')
    if (ada != True):
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')