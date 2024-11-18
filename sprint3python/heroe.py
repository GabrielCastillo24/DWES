class Heroe:
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.ataque = 8
        self.defensa = 5
        self.salud = 100
        self.salud_maxima =100

    #Get/set 
    def get_nombre(self):
        return self.nombre
    
    def get_ataque(self):
        return self.ataque
    
    def get_defensa(self):
        return self.defensa
    
    def get_salud(self):
        return self.salud
    
    def get_salud(self):
        return self.salud

    def get_salud_maxima(self):
        return self.salud_maxima
    

    def atacar(self):
        return self.ataque
    
    def recibir_dano(self, dano):
        # Reduce la salud del héroe al recibir daño.
        self.salud = self.salud - (dano - self.defensa)
        return self.salud # Devuelve el daño real recibido
    

    def curarse(self, cantidad):
        #Restaura la salud del héroe.#
        self.salud = min(self.salud + cantidad, self.salud_maxima)  # No superar la salud máxima
        return self.salud
    
    def subirDefensa(self,cantida):
        #Aumneta la defensa del heroe 
        self.defensa +=self.defensa + cantida
        return self.defensa
    
    def subirAtaque(self,cantida):
        self.ataque = self.ataque + cantida
        
    def estaVivo(self):
        #verifica que si la vida del ehore sea menor que 0 estara muerto, y si no que siga con vida 
        vivo = True 
        if self.salud <=0:
            vivo=False
            return vivo
        else:
            return vivo 


        
  


