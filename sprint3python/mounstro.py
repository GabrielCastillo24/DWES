class Mounstro:
    #Creamos el objeto mounstro
    def __init__(self,nombre):
        self.nombre = nombre
        self.ataque = 6
        self.defensa =3
        self.salud = 15 
    #GET
    def get_nombre(self):
        return self.nombre

    def get_ataque(self):
        return self.ataque
    
    def get_defensa(self):
        return self.defensa
    
    def get_salud(self):
        return self.salud
    

    #METODOS 

    def ataqueM(self,nombre):
        #Devuelve el ataque del mounstro
        return self.ataque,print(f"El mounstro {self.nombre} a atacado a {nombre}")
    
    def mounstroVivo(self):
        vivo = True
        if self.salud <=0:
             vivo = False
             return vivo
        else:
            return vivo

