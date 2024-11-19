from heroe import Heroe #Clase Heroe 
from mounstro import Mounstro #Clase Mounstro
from tesoro import Tesoro #Clase Tesoro 

class Mazmorra:
    #Creamos la mazmorra
    def __init__(self,heroe) :
        self.heroe = heroe
        self.mounstros = Mounstro("lobo")
        self.tesoro = Tesoro()
    #Funcion jugar 
    def jugar(self):
        print(f"{self.heroe.get_nombre()} a entrado a la Mazmorra ...")
        print(f"Te haz encontrado con el mounstro {self.mounstros.get_nombre()} para seguir avanzando tendras que pelear")
        
        #Menu de opciones 
        print("Escogue que haras: ")
        print("atacar pulse : 1")
        print("defender pulse : 2")
        print("curarse : 3")
        print("Salir pulse : x")
        #Creamos bandera para marcar el fin de nuestro bucle 
        bandera = True
        while(bandera):
            print(f"vida de {self.heroe.get_nombre()} : {self.heroe.salud}")
            #Verifica si el mounstro o el heroe tiene vida y si no sale del bucle    
            if(self.mounstros.mounstroVivo() == False or self.heroe.estaVivo == False):
                #verifica si el heroe murio o el mounstro murio para dar el mensaje 
                if(self.heroe.salud < 0):
                    print("El heroe a perdido la batalla")
                    bandera = False
                    break
                else:
                    print(f"{self.heroe.get_nombre()} derroto al mountro")
                    break
            
            #Elige el movimiento 
            movimiento = input("movimiento : ") 
            
            #Si el movimiento es 1 el heroe ataca
            if(movimiento == "1"):
                self.mounstros.salud = self.mounstros.salud - self.heroe.atacar()
                print(f"{self.heroe.get_nombre()} ha atacado al mounstro")
                self.heroe.salud = self.heroe.recibir_dano(self.mounstros.ataque)
                print(f"El mounstro tambien ha atacado ha {self.heroe.get_nombre()}")
            #si el movimiento es 2 el heroe se defiende 
            elif(movimiento == "2"):
                self.heroe.recibir_dano(self.mounstros.ataque) 
                print(f"{self.heroe.get_nombre()} se ha defendido y a resivido poco daño")
            #si el movimiento es 3 el heroe se cura 
            elif(movimiento == "3"):
                print(f"{self.mounstros.get_nombre()} ataca a {self.heroe.get_nombre()}")
                self.heroe.recibir_dano(self.mounstros.ataque)
                self.heroe.curarse(3)
                print(f"{self.heroe.get_nombre()} se a curado  y  restaurado su vida a {self.heroe.salud}")
            #si el movimiento es x sale del juego 
            elif(movimiento == "x"):
                print("Haz salido del juego ")
                bandera =False
                break

            
        print("El mounstro a dejado un tesoro : ")
        #se guarda en variables el tesoro aletorio con la cantidad aletoria de puntos 
        tesoroMazmorra = self.tesoro.tesoroAletorio()
        puntos = self.tesoro.cantidadALetoria()

        #verifica que tipo de recompensa resibe el heroe 
        if(tesoroMazmorra == "ataque"):
            self.heroe.subirAtaque(puntos)
            print(f"{self.heroe.get_nombre()} consigue una espada que aumenta su ataque : +{puntos} atq")
        elif(tesoroMazmorra == "defensa"):
            self.heroe.subirDefensa(puntos)
            print(f"{self.heroe.get_nombre()} consigue un escudo que aumenta su defenza : +{puntos} def")
        elif(tesoroMazmorra == "salud"):
            self.heroe.curarse(puntos)
            print(f"{self.heroe.get_nombre()} consigue un elixir de vida que aumenta su salud : +{puntos} salud")





                
    