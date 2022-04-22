from function import *

def list_game(userid, kepemilikan, datagame):
    arr = []
    for lines in kepemilikan:
        if userid == lines[1]:
            idgame = lines[0]
            for games in datagame:
                if idgame == games[0]:
                    arr += [games]

    print("Daftar game:")

    nomer = 0
    for i in arr:
        nomer += 1
        print(f"{nomer}. {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}" )
    print(">>>")


data_kepemilikan = csv_to_array(r"C:\Users\indra\PycharmProjects\noobman\tubes\kepemilikan.csv")
data_game = csv_to_array(r"C:\Users\indra\PycharmProjects\noobman\tubes\game.csv")

a = input(">>>")

userid = "1"
if a == "list_game":
    list_game(userid, data_kepemilikan, data_game)