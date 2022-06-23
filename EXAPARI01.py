print("EXAMEN PRIMER PARCIAL - Cristian Fuentes Ceron")
print("Hola profe maik !")
print("Recuerda si A > B se hara una suma y su B > A se hara una multiplicacion")
numeroA=int(input("Digite el numero 1"))
numeroB=int(input("Digite el numero 2"))
incremento = 1 
if numeroA > numeroB:
    while incremento <= numeroA:
        numeroB = numeroB + incremento
        incremento +=1
        print("la suma de las series es:",numeroB)

else:
    while incremento <= numeroB:
        numeroA = numeroA * incremento
        incremento +=1
        print("La multiplcacion es ",numeroA)


