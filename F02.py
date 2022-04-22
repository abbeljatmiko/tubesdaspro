from function import *

def UserNameValid (username) :
    #Fungsi yang mengecek apakah username sudah terpakai atau belom
    #True jika username tidak pernah digunakan
    #False jika username sudah tersedia
    UsernameTerpakai = False
    i = 0
    while i < length(username) :
        if username == splitFunc("user.csv")[1] :
            UserNameTerpakai = True
        i+1

def CekUserNameRegister(username) :
    #Fungsi yang memvalidasi username yang diregister
    for i in username :
        if (splitFunc(i)[1] != username) : 
            T = ord(i)
            if 97<=T<=122 or 65<=T<=90 or 48<=T<=57 or T == 95 or T == 45 : 
                return True 
    return False


def register () :
        register_nama = input("Masukan nama: ")
        register_username = input("Masukan username: ")
        password = input("Masukan password: ")
        if UserNameValid(register_username) == True :
            print("Username " + register_username + " sudah terpakai, silakan menggunakan username lain.")
        else :
            if CekUserNameRegister(register_username) == True : 
                print("Username " + register_username + " telah berhasil register ke dalam Binomo")
            elif CekUserNameRegister(register_username) == False :
                print("Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9.")
