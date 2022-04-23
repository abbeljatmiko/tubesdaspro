from function import *
def Login():
    loguser = str(input("Masukan user: "))
    logpass = str(input("Masukkan pass: "))
    f = list(open('user.csv', 'r'))
    k = 0 # Indeks user pada csv file
    j = 0 # Indeks password pada csv file
    a = -1 # Validasi user sesuai dengan password
    b = -2 # Validasi password sesuai dengan user
    validuser = False
    validpass = False
    successful = False
    loggeduser = ''
    for i in f:
        if (splitFunc(i)[1] != loguser):
            #print('Ini k: ',k)
            k += 1
            #print(f'({splitFunc(i)[1]}) = ({loguser})')
        if (splitFunc(i)[1] == loguser):
            #print('k berhasil: ',k)
            #print(' isi k:',splitFunc(i)[1])
            validuser = True
            a = k
    for x in f:
        if ((splitFunc(x)[3]) != logpass) and ((splitFunc(x)[3]) != logpass+"\n"):
            #print('Ini j: ',j)
            j += 1
            #print(f'({(splitFunc(x)[2])}) = ({logpass})')
        if ((splitFunc(x)[3]) == logpass+"\n") or ((splitFunc(x)[3] == logpass)):
            #print('j berhasil: ',j)
            #print(' isi j:',splitFunc(x)[2])
            validpass = True
            b = j
    if (a == b):
        successful = True
    if (validuser == True) and (validpass == True) and (successful == True):
        print(f'Halo {(splitFunc(f[a])[2])}! Selamat datang di “Binomo”.')
        loggeduser = loguser
        return loggeduser, successful # Memberikan nama username, serta validasi logged in (successful optional)
    else: #(successful == False):
        print('Password atau username salah atau tidak ditemukan.')
        successful == False
        return successful # Belum logged-in.
