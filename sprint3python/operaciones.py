
    #Metodo suma
def sumar(valor1,valor2):
    #suma varaible1 mas variable2 
    return valor1 + valor2

#Metodo resta
def restar(valor1,valor2):
    #resta variable 1 menos variable2 
    return valor1 - valor2

#Metodo multiplicar 
def multiplicar(valor1, valor2):
    #Multiplica variable1 por variable2 
    return valor2 * valor2

    #Metodo dividir 
def dividir(valor1, valor2):
    #Comprueba si valor1 es 0, y si lo es muestra un error 
    if valor1 == 0 :
        print("no se puede dividir con 0")
        #Comprueba que si el valor2 es 0, y si lo es muestra un mensaje de error    
    elif valor2 == 0:
        print("no se puede dividir con 0")
        #divide valor1 entre valor2    
    else:
        valor1/valor2



