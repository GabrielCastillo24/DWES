import random
class Tesoro:
    tesoros =["ataque","defensa","salud"]

    def tesoroAletorio(self):
        aletorio = random.randint(0,3)
        cantidad = random.randint(1,6)   
        return [self.tesoros[aletorio], cantidad]
                


