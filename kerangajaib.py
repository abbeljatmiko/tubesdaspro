import time
from function import *

def kerangajaib():

    jawaban = ["Iya", "Tidak", "Yooo ndak tahu kok tanya saya", "sabeb", "masa sihh", "mau", "ah gatau males pengen beli truk", "yakali", "o aja", 
            "gantengg", "tanya aja ke tembok", "di Jakarta", "maybe in your dream", "kerenn pisann maneh"]
    length = length(jawaban)

    input("Apa pertanyaanmu? ")

    local = time.localtime()
    now = time.strftime("%S", local)

    a = 10
    b = 29
    c = 31
    
    count = 0
    loop = True
    now = int(now)                  
    while (count < 7 or loop == True):                          
        if (count >= 7 and (0 <= result <= (length-1))):        
            loop = False
        else:                                   
            result = ((now*a)+b)%c
            now = result                    
            count +=1
        
    print(jawaban[result])
