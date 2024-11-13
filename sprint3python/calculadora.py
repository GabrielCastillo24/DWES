from operaciones import sumar,restar,multiplicar,dividir
def main():
    while True:
        try:
            #Solisitamos los valores al usuario 
            numero1 = float(input("Introduce el primer numero: "))
            numero2 = float(input("introduce el segundo numero: "))
        except ValueError:
            print("Error: Por favor, ingresa valores numéricos válidos.")
            continue  # Volver al inicio del bucle si hay un error de entrada

        #Mensaje al usuario para indicarle que operaciones puede hacer 
        print("Que operaciones quieres realizar")
        print("Para 'suma' pulsa +")
        print("Para 'resta' pulsa -")
        print("Para 'multiplicar' pulsa *")
        print("Para 'dividir' pulsa / ")
            
        #tomamos la operacion del usuario 
        operador = input("Introduce tu operacion : ").strip()
        #comprueba que operacion realiza 
        if operador == '+':
            #llama a la funcion suma 
            resultado = sumar(numero1,numero2)
        elif operador =='-':
            #llama a la funcion resta 
            resultado = restar(numero1,numero2)
        elif operador =='*':
            #llama a la funcion multiplicar 
            resultado = multiplicar(numero1,numero2)
        elif operador == '/':
            #llama a la funcion dividir
            resultado = dividir(numero1,numero2)
        else:
            #error de operador 
            print("operacion invalida")
            
            #muestra el resultado
        print(f"El resultado es: {resultado}")

        repetir = input("Quieres hacer otra operacion s/n : ")

        if repetir != 's':
            print("adios")
            break    
if __name__ == "__main__":
    main()