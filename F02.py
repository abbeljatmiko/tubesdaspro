from function import *

def UserNameValid(username,dfuser) :
    #Fungsi yang mengecek apakah username sudah terpakai atau belom
    #True jika username tidak pernah digunakan
    #False jika username sudah tersedia
    i = 0
    while i < length(dfuser) :
        if username == dfuser[i][1]:
            return True
        i += 1
    return False

def CekUserNameRegister(username) :
    #Fungsi yang memvalidasi username yang diregister
    for i in username :
        T = ord(i)
        if not (97<=T<=122 or 65<=T<=90 or 48<=T<=57 or T == 95 or T == 45) :
            return False
    return True

def register() :
        register_nama = input("Masukan nama: ")
        register_username = input("Masukan username: ")
        password = input("Masukan password: ")
        if UserNameValid(register_username) == True :
            print("Username " + register_username + " sudah terpakai, silakan menggunakan username lain.")
        else :
            if CekUserNameRegister(register_username) == True : 
                print("Username " + register_username + " telah berhasil register ke dalam Binomo")
                berhasil = True
            elif CekUserNameRegister(register_username) == False :
                print("Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9.")
                berhasil = False
        return berhasil