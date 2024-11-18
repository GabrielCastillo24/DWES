from heroe import Heroe #Clase Heroe 
from mounstro import Mounstro #Clase Mounstro
from tesoro import Tesoro #Clase Tesoro 

class Mazmorra:
    #Creamos la mazmorra
    def __init__(self,heroe) :
        self.heroe = heroe
        self.mounstros = Mounstro("lobo")
        self.tesoro = Tesoro()

    def jugar(self):
        print(f"{self.heroe.get_nombre()} a entrado a la Mazmorra ...")
        print(f"Te haz encontrado con el mounstro {self.mounstros.get_nombre()} para seguir avanzando tendras que pelear")
        
        print("Escogue que haras: ")
        print("atacar pulse : 1")
        print("defender pulse : 2")
        print("curarse : 3")
        print("Salir pulse : x")

        bandera = True
        while(bandera):
            print(f"vida de {self.heroe.get_nombre()} : {self.heroe.salud}")   
            if(self.mounstros.mounstroVivo() == False or self.heroe.estaVivo == False):
                print(f"vida del mountro{self.mounstros.salud}")
                bandera = False
                break
            
            movimiento = input("movimiento : ") 
            
            if(movimiento == "1"):
                self.mounstros.salud = self.mounstros.salud - self.heroe.atacar()
                print(f"{self.heroe.get_nombre()} ha atacado al mounstro")
                self.heroe.salud = self.heroe.recibir_dano(self.mounstros.ataque)
                print(f"El mounstro tambien ha atacado ha {self.heroe.get_nombre()}")
            elif(movimiento == "2"):
                self.heroe.recibir_dano(self.mounstros.ataque) 
                print(f"{self.heroe.get_nombre()} se ha defendido y a resivido poco daño")
            elif(movimiento == "3"):
                print(f"{self.mounstros.get_nombre()} ataca a {self.heroe.get_nombre()}")
                self.heroe.recibir_dano(self.mounstros.ataque)
                self.heroe.curarse(3)
                print(f"{self.heroe.get_nombre()} se a curado  y  restaurado su vida a {self.heroe.salud}")
            elif(movimiento == "x"):
                print("Haz salido del juego ")
                bandera =False
                break

            
        print("El mounstro a dejado un tesoro : ")
        tesoroMazmorra = self.tesoro.tesoroAletorio()
        puntos = self.tesoro.cantidadALetoria()

        if(tesoroMazmorra == "ataque"):
            self.heroe.subirAtaque(puntos)
            print(f"{self.heroe.get_nombre()} consigue una espada que aumenta su ataque : +{puntos} atq")
        elif(tesoroMazmorra == "defensa"):
            self.heroe.subirDefensa(puntos)
            print(f"{self.heroe.get_nombre()} consigue un escudo que aumenta su defenza : +{puntos} def")
        elif(tesoroMazmorra == "salud"):
            self.heroe.curarse(puntos)
            print(f"{self.heroe.get_nombre()} consigue un elixir de vida que aumenta su salud : +{puntos} salud")





                
    