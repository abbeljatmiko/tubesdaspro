from function import *


def list_game(userid, kepemilikan, datagame):
    arr = []
    for lines in kepemilikan:
        if str(userid) == lines[1]:
            idgame = lines[0]
            for games in datagame:
                if idgame == games[0]:
                    arr += [games]

    print("Daftar game:")

    nomer = 0
    for i in arr:
        nomer += 1
        print(f"{nomer}. {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}" )
