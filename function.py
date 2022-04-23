def length(listx):
    n = 0
    global length
    for i in listx:
        n += 1
    return n



def sortlist(x):
    for i in range(length(x) -1):
        for j in range(length(x) -i -1):
            if x[j] > x[j+1] :          
                sementara = x[j]                         
                x[j] = x[j+1]
                x[j+1] = sementara

def csv_to_array(dir):
    f = open(dir, 'r')
    raw_data = f.readlines()
    f.close()

    matrix_data = [['']]
    index_matrix = 0

    for line in raw_data:
        index_array = 0

        for c in line:
            if c == ';':
                matrix_data[index_matrix] += ['']
                index_array += 1
            elif c != '\n':
                matrix_data[index_matrix][index_array] += c

        if line != raw_data[-1]: matrix_data += [['']]
        index_matrix += 1

    return matrix_data

def cek_int(string) :
    cek=True

    for i in string :
        if(i<'0' or i>'9') :
            cek=False 

    return cek

def convert_string(list) :
    list_n=[]
    len=length(list)
    index=0
    temp=0
    for i in range(1,len) :
        
        if(i==len-1) :
            list_n+=[list[temp:i]]

            if(list[-1:]!="\n"):
                list_n[index]=list_n[index]+list[len-1]

            if(cek_int(list_n[index])) :
                list_n[index]=int(list_n[index])
                        
        else:
            if(list[i]==';') :
                index+=1
                string=list[temp:i]
                if(cek_int(string)) :
                    list_n=list_n+[int(string)]
                else :
                    list_n=list_n+[string]
                temp=i+1
    return list_n

def splitFunc(x): # Split 6 kata
    first_val = ''
    second_val = ''
    third_val = ''
    fourth_val = ''
    fifth_val = ''
    sixth_val = ''
    i = 0
    terminate_search = False

    while (terminate_search != True): #Mendapatkan first_val (ID)
        if (x[i] != ','):
            first_val += x[i]
            i += 1
        else:
            while (terminate_search != True): # Mendapatkan second_val (username)
                if (x[i+1] != ','):
                    second_val += x[i+1]
                    i += 1
                else:
                    while(terminate_search != True): # Mendapatkan third_val (nama)
                        if(x[i+2] != ','):
                            third_val += x[i+2]
                            i +=1
                        else:
                            while(terminate_search != True): # Mendapatkan fourth_val (password)
                                if(x[i+3] != ','):
                                    fourth_val += x[i+3]
                                    i+=1
                                else:
                                    while(terminate_search != True): # Mendapatkan fifth_val (role)
                                        if(x[i+4] != ','):
                                            fifth_val += x[i+4]
                                            i+=1
                                        else:
                                            while(terminate_search != True): # Mendapatkan sixth_val (saldo)
                                                if(x[i+5] != ','):
                                                    sixth_val += x[i+4+1:]
                                                    terminate_search = True
    return(first_val, second_val, third_val, fourth_val, fifth_val, sixth_val)

def splitFunct(x): # Split 5 kata
    first_val = ''
    second_val = ''
    third_val = ''
    fourth_val = ''
    fifth_val = ''
    i = 0
    terminate_search = False

    while (terminate_search != True): #Mendapatkan first_val (ID)
        if (x[i] != ','):
            first_val += x[i]
            i += 1
        else:
            while (terminate_search != True): # Mendapatkan second_val (Nama game)
                if (x[i+1] != ','):
                    second_val += x[i+1]
                    i += 1
                else:
                    while(terminate_search != True): # Mendapatkan third_val (Harga)
                        if(x[i+2] != ','):
                            third_val += x[i+2]
                            i +=1
                        else:
                            while(terminate_search != True): # Mendapatkan fourth_val (kategori)
                                if(x[i+3] != ','):
                                    fourth_val += x[i+3]
                                    i+=1
                                else:
                                    while(terminate_search != True): # Mendapatkan fifth_val (tahun_rilis)
                                        if(x[i+4] != ','):
                                            fifth_val += x[i+3+1:]
                                            terminate_search = True
    return(first_val, second_val, third_val, fourth_val, fifth_val)

def splitFunction(x):
    first = ''
    second = ''
    i = 0
    terminate = False
    while (terminate != True):
        if (x[i] != ','):
            first += x[i]
            i+=1
        else:
            second += x[i+1:]
            terminate = True
    return (first, second)

def csv_to_array(dir):
    f = open(dir, 'r')
    raw_data = f.readlines()
    f.close()

    matrix_data = [['']]
    index_matrix = 0

    for line in raw_data:
        index_array = 0

        for c in line:
            if c == ';':
                matrix_data[index_matrix] += ['']
                index_array += 1
            elif c != '\n':
                matrix_data[index_matrix][index_array] += c

        if line != raw_data[-1]: matrix_data += [['']]
        index_matrix += 1

    return matrix_data


def print_data_game(array_data):
    def panjang(elmt):
        ln = 0
        for i in elmt:
            ln += 1
        return ln

    panjang_maks = [0, 0, 0, 0, 0]
    nama_maks = 0
    ktgr_maks = 0
    hrga_maks = 0

    for line in array_data:
        if line[0] != 'id':
            n = panjang(line[1])
            k = panjang(line[2])
            h = panjang(line[4])
            if n > nama_maks: nama_maks = n
            if k > ktgr_maks: ktgr_maks = k
            if h > hrga_maks: hrga_maks = h

    indeks = 1
    for line in array_data:
        if line[0] != 'id':
            print(f'{indeks}. ', end='')
            for i in range(5):
                if i == 1:
                    print(line[i], ' ' * (nama_maks - panjang(line[i])), '|  ', end='')
                elif i == 2:
                    print(line[i], ' ' * (ktgr_maks - panjang(line[i])), '|  ', end='')
                elif i == 4:
                    print(line[i], ' ' * (hrga_maks - panjang(line[i])), '|  ', end='')
                else:
                    print(line[i], ' |  ', end='')
            print(line[5])
            indeks += 1


def array_to_string(arr):
    converted_data = ''
    for line in arr:
        for elmt in line:
            converted_data += str(elmt)
            if elmt != line[-1]:
                converted_data += ';'
        converted_data += '\n'
    return converted_data


def get_index(game_id):
    return int(game_id[4]) * 100 + int(game_id[5]) * 10 + int(game_id[6])

def maxs(x,y) :
    if(x>y) :
        return x 
    else :
        return y

def print_data(data) :
    max=[0 for i in range(length(data[0]))]

    for i in range(length(data)) :
        if(i==0) :
            for j in range(length(data[0])) :
                max[j]=length(str(data[i][j]))
        else :
            for j in range(length(data[0])) :
                max[j]=maxs(max[j],length(data[i][j]))

    for i in range(length(data)) :
        print(f"{(i+1)}. ",end='')
        for j in range(length(data[0])) :
            if(j==0) :
                print(f"{data[i][j] : <{max[j]}} ",end='')
            else :
                print(f"| {data[i][j] : <{max[j]}} ",end='')
        print()

def get_data(file) :
    f=open(file).readlines()
    data=[]
    for i in f :
        data=data+[convert_string(i)]
    return data

def array_to_csv()
