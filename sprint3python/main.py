from heroe import Heroe
from mazmorra import Mazmorra

def main():

    nombreHeroe = input("Introduce un nombre de heroe : ")
    
    heroe = Heroe(nombreHeroe)
    
    mazmorra = Mazmorra(heroe)

    mazmorra.jugar()
    

if __name__ == "__main__":
    main()