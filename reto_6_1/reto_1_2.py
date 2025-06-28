def detectorpalindromo(word):
    if not isinstance(word,(str)):
        raise ValueError("el dato ingresado no es una cadena de caracteres") #captamos el error cuando se ingresa un dato que no es una cadena de caracteres
    long=(len(word)) #longitud de la palabra
    i=0
    s:list=[]
    e:list=[]
    for j in word:
        if long%2==0: #caso par
            if i<long/2:s.append(j) #primera mitad
            if i>=long/2: e.append(j) #segunda mitad
        else: #caso impar
            if i<(long-1)/2:s.append(j) #primera mitad 
            if i>(long-1)/2:e.append(j) #segunda mitad       
        i=i+1
    if sorted(s)==sorted(e): #comparamos ambas mitades ordenadas
        print("Es un palindromo")
    else:
        print("No es un palindromo")    
if __name__ == '__main__':
    detectorpalindromo("reconocer")
    detectorpalindromo("reconocer123")
    detectorpalindromo(1234)
   
        
    