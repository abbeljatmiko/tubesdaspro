from function import *
def riwayat(loggeduser):
    idx = 0 # Jumlah baris pada riwayat.csv (data)
    c = 0 # Pengurutan nomor output
    ada = False # Apabila tidak ada riwayat pembelian
    f = list(open('riwayat.csv', 'r'))
    print('Daftar game:')
    for i in f:
        idx +=1
    for j in range(1, idx):
        r = splitFunct(f[j])
        for k in r:
            if (k == loggeduser):
                c+=1
                print(f'{c}.',end=" ")
                ada = True
                for o in range(5):
                    if o < 4:
                        print(r[o],' |', end=' ')
                    else:
                        print(r[o], end='')
    if ada != True:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')