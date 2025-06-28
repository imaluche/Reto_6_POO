def oper(a,b,o): #definimos la funcion con 3 entradas. Los dos operandos y el operador
    if  isinstance(a,(list,str)) or isinstance(b,(list,str)):
        raise TypeError("Los operandos deben ser datos del tipo int o float") #captamos el error cuando se ingresan datos no numericos
    if o == '+':
        return float(a) + float(b)
    if o== '-':
        return float(a) - float(b)
    if o == '*':
        return float(a) * float(b)
    if o == '/':
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero") #por medio de un zerodivisionerror captamos el error cuando se usa la funcion para dividir entre cero
        return float(a) / float(b)
    # la variable o permite que la funcion reconozca directamente los simbolos de cada operador para hacer la operacion deseada
if __name__=="__main__":
    print("el resultado es "+ str(oper(3,0,'/'))) #llamamos a la funcion oper y le pasamos los parametros
 