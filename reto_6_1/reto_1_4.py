from reto_1_3 import * #importamos las funciones del punto anterior
def mayor(l):
    if not isinstance(l,(list)): #verificamos que el dato ingresado sea una lista
        raise ValueError("El dato ingresado no es una lista") #captamos el error cuando se ingresa un dato que no es una lista
    l.sort(reverse=True) #ordenamos la lista ingresada de mayor a menor
    if not isinstance(l[0],float) or not isinstance(l[1],float):
        raise TypeError("La lista debe estar compuesta solamente por numeros")
    print("la mayor suma es: "+ str(l[0]+l[1])) #sumamos el primer y segundo elemento
if __name__=="__main__":
    n=int(input("Cuantos numeros quieres sumar? "))
    x=generar_lista(n)
    mayor(x)