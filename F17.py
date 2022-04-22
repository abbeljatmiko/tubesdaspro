def Exit():
    x = ''
    while not (x == Y) or (x == y) or (x == n) or (x == N):
        x = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')
    
    if (x == Y) or (x == y):
        save()
    # else, tidak di save