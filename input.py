import listas
#from methods import anhadirShawarma as anhadirShawarma
#from methods import anhadirProducto as anhadirProducto
from methods import *

listasTiposList = listas.listasTiposList
tipoProdList = listas.tipoProdList
individualesList = listas.individualesList
combosPersonalesList = listas.combosPersonalesList
combos2MasList = listas.combos2MasList
extrasList = listas.extrasList
adicionalesList = listas.adicionalesList


# Data Structure:
# ticket:       list of itemT ->    [[], [], ..., []]
# orden:        list of itemO ->    [[], [], ..., []]
# itemT:        if shawarma: [categoria, producto, extra, adicional, precio], elif bebida: [categoria, producto, precio], elif papas: [categoria, producto, adicional, precio]     -> categoria: 0: shawarma, 1: bebida, 2: papas
# itemO:        if shawarma: [producto, extra, adicional, cremas], elif bebida: [producto], elif papas: [producto, adicional]


textInicio = "1. Presione (1) para iniciar\n2. Presione (2) para añadir producto\n3. Presione (3) para ver la orden\n4. Presione (4) para confirmar y finalizar"

while(True):
    print(textInicio)
    '''
    1. Presione (1) para iniciar
    2. Presione (2) para añadir producto
    3. Presione (3) para ver la orden
    4. Presione (4) para confirmar y finalizar
    '''

    inicio = input()
    if inicio == "1":
        # crear orden, crear ticket, cuenta = 0
        #cTicket()
        ordenAc = cOrden()
        
        anhadirProducto(orden = ordenAc)

    elif inicio == "2":
        print("Usted desea añadir un nuevo producto, continúe")
        anhadirProducto()

    elif inicio == "3":
        # imprimir datos en pantalla
        #rOrden()
        print("Esta es la orden: ", "gg")

    elif inicio == "4":
        # mostrar pedido, tanto orden como ticket, enviar a cocina y facturar
        # borrar ticket de temporal y mandarlo a BBDD o permanente
        print("Orden confirmada")
        break
        
    else:
        print("Ha seleccionado un valor incorrecto")

