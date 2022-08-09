from secrets import randbelow
from time import sleep
import json 

charEsp = "!#$%&/()=?¡¨*][}{-_\\' "
charLow = "qazwsxedcrfvtgbyhnujmikolp"
numChars = "1234567890"
charsUp = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
charsFull = charEsp + charLow + numChars + charsUp


def create(largo:int)->int:
    if largo == None:
        print("Error..")
        exit()
    print("Generando...")
    sleep(1)
    newCont = ""
    for i in range(largo):
        newChar = charsFull[randbelow(81)]
        newCont += newChar
    return newCont

def login(ctr:str)->str:
    sleep(1)
    with open("directory", "r") as file:
        data = json.load(file)
        txt = data["root"]
        if ctr == txt: return 1
        else: return 0

        # El with cierra el archivo cuando termina el codigo

def look():
    sleep(1)
    with open("directory of json", "r") as file:
        data = json.load(file)
        txt = data["passwords"]
        for i in txt:
            try:
                print(f" {i} ")
            except:
                print(txt)
                print(i)

def add(ctrAdd:str)->str:
    sleep(1)
    try:
        with open ("directory of jason") as file:
            rescribe = open("/Users/carlo/Desktop/data.json",'r+')
            data = json.load(file)
            data['passwords']+=[ctrAdd]
            json.dump(data,rescribe,indent=4)
            """data = json.load(file)
            print(data)
            #data["passwords"].append(ctrAdd)
            #json.dump(data, file)
            print(data)
            """
            print("Contraseña ingresada con exito!!")
            
    except:
        print("No se pudo ingresar la contraseña...")
        
