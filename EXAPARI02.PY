print("Hola ESTA ES UNA MAQUINA DE BEBIDAS")
print("A = COCA COLA , B = SPRITE , C = SENSAO")
print("Selecciona la bebida que deseas")
print("A = $270")
print("B = $340")
print("C = $390")
bebida = input()
cantidad = 0
cambio = 0 
if bebida == "A" or bebida == "B" or bebida == "C":
    if bebida == "A":
        print("Precio de $270")
        precio = 270
        while cantidad < precio:
            print("Ingresa las monedas o billetes")
            print("1 = $10")
            print("2 = $50")
            print("3 = $100")
            moneda =int(input())
            if moneda == 1 or moneda == 2 or moneda == 3:
                if moneda == 1:
                    cantidad = cantidad + 10
                else:
                    if moneda == 2:
                        cantidad = cantidad + 50 
                    else:
                        cantidad = cantidad + 100
            else:
                print("No aceptamos estas monedas , ingresa la correcta")
            print("El precio del producto es $",precio)
            print("Ingreso $",cantidad)
        if cantidad > precio:
            cambio = cantidad - precio
            while cambio > 0 :
                if cambio >= 50:
                    print("su cambio es de : $ 50")
                    cambio = cambio -50
                if cambio < 50:
                    print("Su cambio es de $10")
                    cambio = cambio -10  
            
    if bebida == "B":
        print("Precio de $340")
        precio = 340
        while cantidad < precio:
            print("Ingresa las monedas o billetes")
            print("1 = $10")
            print("2 = $50")
            print("3 = $100")
            moneda =int(input())
            if moneda == 1 or moneda == 2 or moneda == 3:
                if moneda == 1:
                    cantidad = cantidad + 10
                else:
                    if moneda == 2:
                        cantidad = cantidad + 50 
                    else:
                        cantidad = cantidad + 100
            else:
                print("No aceptamos estas monedas , ingresa la correcta")
            print("El precio del producto es $",precio)
            print("Ingreso $",cantidad)
        if cantidad > precio:
            cambio = cantidad - precio
            while cambio > 0 :
                if cambio >= 50:
                    print("su cambio es de : $ 50")
                    cambio = cambio -50
                if cambio < 50:
                    print("Su cambio es de $10")
                    cambio = cambio -10
    if bebida == "C":
        print("Precio de $390")
        precio = 390
        while cantidad < precio:
            print("Ingresa las monedas o billetes")
            print("1 = $10")
            print("2 = $50")
            print("3 = $100")
            moneda =int(input())
            if moneda == 1 or moneda == 2 or moneda == 3:
                if moneda == 1:
                    cantidad = cantidad + 10
                else:
                    if moneda == 2:
                        cantidad = cantidad + 50 
                    else:
                        cantidad = cantidad + 100
            else:
                print("No aceptamos estas monedas , ingresa la correcta")
            print("El precio del producto es $",precio)
            print("Ingreso $",cantidad)
        if cantidad > precio:
            cambio = cantidad - precio
            while cambio > 0 :
                if cambio >= 50:
                    print("su cambio es de : $ 50")
                    cambio = cambio -50
                if cambio < 50:
                    print("Su cambio es de $10")
                    cambio = cambio -10
else:
    print("Ingresa el articulo correcto")
    


