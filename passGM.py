'''
problema:
Crear una generador y gestionador de 
contraseñas donde tendras que usar archivo txt 
para guardar un usuario(tipo root) donde gestionaras
tus contraseñas pero estas seran encriptadas 
para pasarlas posteriormente al txt
'''

#Seleccionar
from time import sleep
from passGMF import create,login,look,add

while True:
    sl = input("Ingresa un caracter:\n C : Crear contraseñas\n G : Gestionar contraseñas\n E : Salir\n").lower()
    if sl == "g" or sl == "c" or sl == "e": break 
    print("Porfavor ingresa un caracter disponible...")

if sl == "c":
    largo = int(input("Ingresa la longitud de tu contraseña nueva:\n"))
    contra = create(largo)
    print(contra)
    input("Enter para salir...")
    sleep(2)
    exit()

elif sl == "g":
    contra = input(" Ingresa la contraseña del root...\n")
    new = login(ctr=contra)
    if new == 1: 
        print("\n ¡Contraseña correcta!")
        pass
    else:
        print("\n Contraseña incorrecta...")
        input("Enter para salir...")
        sleep(2)
        exit()

else:
    input("Enter para salir...")
    print("\nSaliendo...")
    sleep(2)
    exit()


while True:
    sl = input("\nIngresa un caracter:\n 1 : Revisar contraseñas\n 2 : Agregar contraseñas\n 3 : Salir\n")
    if sl == "1" or sl == "2" or sl == "3": break
    print("Porfavor ingresa un caracter disponible...")
    sleep(1)

if sl == "1":
    print("\nTus contraseñas Carlos:")
    look()
    input("Enter para salir...")
    sleep(2)
    exit()
elif sl == "2":
    contra = input("\n Agrega la contraseña:\n")
    add(contra)
    input("Enter para salir...")
    sleep(2)
    exit()
else: 
    input("Enter para salir...")
    print("\nSaliendo...")
    sleep(2)
    exit()
