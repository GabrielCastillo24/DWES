from heroe import Heroe
from mazmorra import Mazmorra

def main():
    #Pedimos el nombre del heroe por consola 
    nombreHeroe = input("Introduce un nombre de heroe : ")
    #Creamos el heroe 
    heroe = Heroe(nombreHeroe)
    
    #Creamos la mazmorra con el heroe 
    mazmorra = Mazmorra(heroe)

    #Lamada al metodo jugar()
    mazmorra.jugar()
    

if __name__ == "__main__":
    main()