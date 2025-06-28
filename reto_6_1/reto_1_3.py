def generar_lista(n):
    if not isinstance(n, int) or int (n) <= 0:
        raise ValueError("El numero debe ser un entero positivo") 
    lista:list=[]
    for j in range(n):
        num=int(input("Escribe el numero (en caso de no ser entero se convertira a un entero): "))
        lista.append(num)
    print("Tu lista es: "+ str(lista))
    return lista
def primos(li):
    if not isinstance(li, list):
        raise ValueError("El dato ingresado no es una lista") #captamos el error cuando se ingresa un dato que no es una lista
    prime:list=[]
    for val in li:
        if not isinstance(val,int):
            raise TypeError("la lista debe estar compuesta solamente por numeros") # recorremos la lista
        div:int=0
        comprobador:int=1
        while comprobador<=val:
            if val%comprobador==0:# comprobamos en que caso la division es entera
                div=div+1
            comprobador=comprobador+1
        if div==2: # un primo solo se puede dividir por 1 y por si mismo
            prime.append(val)
    print("los numeros primos de tu lista eran: "+ str(prime))
if __name__=="__main__":
    x = int(input("Cuantos numeros quieres ingresar a tu lista: "))
    listado:list = generar_lista(x)
    primos(listado)
    lista2 = "nohaylista"
    primos(lista2)
    primos([1,2,3,4,5,"eee"])