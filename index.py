
#FECHA 08/09/23 6:56 PM

print("Hello world, welcome to store")

#---------------------------------
#Ingresos//
#Lechuga= Precio 1.55 // Ingreso % = 15% // Precio unidad 1.79 // Impuesto N° 21% // Final 2.17
#Tomate = Precio 0.52 // Ingreso % = 15% // Precio unidad 0.60 // Impuesto N° 21% // FInal 0.73
#Pollo  = Precio 1.34 // Ingreso % = 12% // Precio unidad 1.51 // Impuesto N° 21% // FInal 1.83
#Pan    = Precio 0.71 // Ingreso % = 12% // Precio unidad 0.80 // Impuesto F° 10% // FInal 0.88
#Maiz   = Precio 1.21 // Ingreso % = 12% // Precio unidad 1.36 // Impuesto F° 10% // FInal 1.50
#---------------------------------

#DESCUENTOS
descuentos = {"PROMO_5":5,"PROMO_10":10}

prod = {"LECHUGA":2.17,"TOMATE":0.73,"POLLO":1.83,"PAN":0.88,"MAIZ":1.50}
total = 0
totalr = 0
print("PRODUCTOS: ",prod)
while True:  
    preg = int(input("Deseas comprar un articulo? SI=1 NO=2 :"))
    if preg==1:
        selec_artic = str(input("Selecciona el articulo: ").upper())
        if selec_artic in prod:
            selec = prod[selec_artic]
            print("Tu compra es: ",selec)
            total += selec
            totalr = round(total)
        else:
            print("El articulo no se encuentra en venta")
    elif preg==2:
        break
    else:
        print("No has elegido alguna opcion correcta")

print("TOTAL DE LA COMPRA: ",total)   
print("TOTAL DE LA COMPRA REDONDEADAA:",totalr)

"""
ANOTACIONES PROYECTO//
VIDEO Django Fazt = Parte Django Shell
---// Hasta ahora se creo el entorno virtual, se uso el entorno virtual, se instalo Django, se creo proyecto,
    Explico estructura del proyecto,se creo app, se imprimio en navegador el primer hola mundo,se hizo un 
    include para organizar mejor las urls, se descargo SqBrowser y se creo modelos,para base de datos,se esta
    interactuando con DjangoShell para agregar datos desde DbBrowser,
"""