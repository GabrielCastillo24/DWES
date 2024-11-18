import random
class Tesoro:
    def __init__(self):
        self.tesoros =["ataque","defensa","salud"]
        self.cantidadRandom = 0

    def tesoroAletorio(self):
        aletorio = random.randint(0,2)
        bonificacion = self.tesoros[aletorio]  
        return bonificacion
    
    def cantidadALetoria(self):
        self.cantidadRandom =  random.randint(0,5)
        return self.cantidadRandom
                


