import strs
import listas

inputTextAdicionales = strs.inputTextAdicionales
inputTextExtras = strs.inputTextExtras
inputTextTipoProd = strs.inputTextTipoProd
inputTextCombosPersonales = strs.inputTextCombosPersonales
inputTextCombos2Mas = strs.inputTextCombos2Mas
inputTextInvividuales = strs.inputTextInvividuales


listasTiposList = listas.listasTiposList
tipoProdList = listas.tipoProdList
individualesList = listas.individualesList
combosPersonalesList = listas.combosPersonalesList
combos2MasList = listas.combos2MasList
extrasList = listas.extrasList
adicionalesList = listas.adicionalesList


def anhadirShawarma(saborShawarma = None):
    #itemTTemp = list()
    #itemTTemp.append("0")                                                    # categoria
    itemOTemp = list()
    if saborShawarma != None:
        inputIndividual = saborShawarma
        # crear item, inicializar con sabor de shawarma
        #cItem(orden, saborShawarma)
        
        #itemTTemp.append(individualesList[int(inputIndividual)-1][0])            # producto
        itemOTemp.append((individualesList[int(inputIndividual)-1][0]))
    else:
        print(strs.inputTextInvividuales)
        inputIndividual = input()
        # crear item, inicializar con sabor de shawarma
        #itemTTemp.append(individualesList[int(inputIndividual)-1][0])            # producto
        itemOTemp.append(individualesList[int(inputIndividual)-1][0])
    
    adicional = list()
    strAdicional = ""
    while(True):
        ifAdicional = input("¿Desea añadir algún adicional? (1) Sí, (2) No: ")
        if ifAdicional == "1":
            print(inputTextAdicionales)
            inputAdicional = input()
            if int(inputAdicional) < len(adicionalesList)+1:
            # adicional = adicionalesList[inputAdicional-1]
                adicional.append(adicionalesList[int(inputAdicional)-1][0])
            #añadir adicional
                strAdicional = adicional[0]
                for i in range(1, len(adicional)):
                    strAdicional = strAdicional + ", " + adicional[i]
                print("Los adicionales son:", strAdicional)
            else:
                print("Ha seleccionado un valor incorrecto")
        elif ifAdicional == "2":
            if len(adicional) == 0:
                print("Sin adicionales")
            elif len(adicional) > 0:
                strAdicional = adicional[0]
                for i in range(len(adicional)):
                    strAdicional = strAdicional + ", " + adicional[i]
                print("Los adicionales son:", strAdicional)
            else:
                print("error inesperado")
            break
        else:
            print("Ha seleccionado un valor incorrecto.\n")
    itemOTemp.append(adicional)                                              # adicional

    ifExtra = input("¿Desea añadir algún extra? (1) Sí, (2) No: ")
    extras = list()
    if ifExtra == "1":
        print(inputTextExtras)
        inputExtra = input()
        if inputExtra == "1":
            extras.append(extrasList[int(inputExtra)-1])
            print("Shawarma con extra pollo (+50%)")
            # añadir extra
        elif inputExtra == "2":
            extras.append(extrasList[int(inputExtra)-1])
            print("Se ha añadido una (1) chicha y papas nativas personales")
            #añadir chicha y papas personales
        elif inputExtra == "3":
            print("No aplica a shawarmas")
        else:
            print("Ha seleccionado un valor incorrecto")
    elif ifExtra == "2":
        print("Sin extras")
    else:
        print("Ha seleccionado un valor incorrecto")
    itemOTemp.append(extras)                                                   # extras
    ifCremas = input("¿Desea añadir cremas? (1) Sí, (2) No: ")
    if ifCremas == "1":
        inputCremas = input("Ingrese el detalle de las cremas: ")
        if inputIndividual == "5":
        #   añadir ají de cocona
            inputCremas = inputCremas + ", Charapita"
        #añadir cremas
        itemOTemp.append(inputCremas)
    elif ifCremas == "2":
        print("No se añadieron cremas")
    else:
        print("Ha seleccionado un valor incorrecto")
    return itemOTemp

def anhadirProducto(orden):
    print(inputTextTipoProd)
    inputTipoProd = input()
    if inputTipoProd == "1":
        prod = anhadirShawarma()
        print("Shawarma añadida")
        orden.append(prod)
        print(prod)

    elif inputTipoProd == "2":
        print(inputTextCombosPersonales)
        inputCombosPersonales = input()
        
        if inputCombosPersonales == "1":
            prod = anhadirShawarma(saborShawarma="1")
            orden.append(prod)
            print(prod)
            # añadir papas nativas personales
            temp = [adicionalesList[7]]
            orden.append(temp)
            # añadir bebida
            temp = [adicionalesList[9]]
            orden.append(temp)

        elif inputCombosPersonales == "2":
            prod = anhadirShawarma(saborShawarma="2")
            orden.append(prod)
            # añadir papas nativas personales
            temp = [adicionalesList[7]]
            orden.append(temp)
            # añadir bebida
            temp = [adicionalesList[9]]
            orden.append(temp)
            rOrden(orden)

        elif inputCombosPersonales == "3":
            prod = anhadirShawarma("3")
            orden.append(prod)
            # añadir papas nativas personales
            temp = [adicionalesList[7]]
            orden.append(temp)
            # añadir bebida
            temp = [adicionalesList[9]]
            orden.append(temp)

        elif inputCombosPersonales == "4":
            prod = anhadirShawarma("4")
            orden.append(prod)
            # añadir papas nativas personales
            temp = [adicionalesList[7]]
            orden.append(temp)
            # añadir bebida
            temp = [adicionalesList[9]]
            orden.append(temp)

        elif inputCombosPersonales == "5":
            prod = anhadirShawarma("5")
            orden.append(prod)
            # añadir papas nativas personales
            temp = [adicionalesList[7]]
            orden.append(temp)
            # añadir bebida
            temp = [adicionalesList[9]]
            orden.append(temp)
        
        elif inputCombosPersonales == "6":
            prod = anhadirShawarma("6")
            orden.append(prod)
            # añadir papas nativas personales
            temp = [adicionalesList[7]]
            orden.append(temp)
            # añadir bebida
            temp = [adicionalesList[9]]
            orden.append(temp)

        else:
            print("Ha seleccionado un valor incorrecto")

    elif inputTipoProd == "3":
        print(inputTextCombos2Mas)
        inputCombos2Mas = input()
        if inputCombos2Mas == "1":
            prod = anhadirShawarma("1")
            orden.append(prod)
            prod = anhadirShawarma("1")
            orden.append(prod)

            # añadir Papas Nativas Grande
            # añadir bebida 1 Litro
            temp = ["Papas Nativas Grande"]
            orden.append(temp)
            temp = [adicionalesList[9]]
            orden.append(temp)
            orden.append(temp)
        elif inputCombos2Mas == "2":
            print(inputTextInvividuales)
            sh1 = input()
            sh1 = int(sh1)
            prod = anhadirShawarma(saborShawarma=individualesList[sh1[0]])
            orden.append(prod)
            print("Primera shawarma añadida")
            print(inputTextInvividuales)
            sh2 = input()
            sh2 = int(sh2)
            prod = anhadirShawarma(saborShawarma=individualesList[sh2][0])
            orden.append(prod)
            print("Segunda shawarma añadida")
            # añadir Papas Nativas Grande
            # añadir bebida 1 Litro
            temp = ["Papas Nativas Grande"]
            orden.append(temp)
            temp = [adicionalesList[9]]
            orden.append(temp)
            orden.append(temp)
        elif inputCombos2Mas == "3":
            print(inputTextInvividuales)
            sh1 = input()
            sh1 = int(sh1)
            prod = anhadirShawarma(saborShawarma=individualesList[sh1][0])
            orden.append(prod)
            print("Primera shawarma añadida")
            print(inputTextInvividuales)
            sh2 = input()
            sh2 = int(sh2)
            prod = anhadirShawarma(saborShawarma=individualesList[sh2][0])
            orden.append(prod)
            print("Segunda shawarma añadida")
            print(inputTextInvividuales)
            sh3 = input()
            sh3 = int(sh3)
            prod = anhadirShawarma(saborShawarma=individualesList[sh3][0])
            orden.append(prod)
            print("Tercera shawarma añadida")
            # añadir Papas Nativas Grande
            # añadir bebida 1 Litro
            temp = ["Papas Nativas Grande"]
            orden.append(temp)
            temp = [adicionalesList[9]]
            orden.append(temp)
            orden.append(temp)
        elif inputCombos2Mas == "4":
            print(inputTextInvividuales)
            sh1 = input()
            sh1 = int(sh1)
            prod = anhadirShawarma(saborShawarma=individualesList[sh1][0])
            orden.append(prod)
            print("Primera shawarma añadida")
            print(inputTextInvividuales)
            sh2 = input()
            sh2 = int(sh2)
            prod = anhadirShawarma(saborShawarma=individualesList[sh2][0])
            orden.append(prod)
            print("Segunda shawarma añadida")
            print(inputTextInvividuales)
            sh3 = input()
            sh3 = int(sh3)
            prod = anhadirShawarma(saborShawarma=individualesList[sh3][0])
            orden.append(prod)
            print("Tercera shawarma añadida")
            print(inputTextInvividuales)
            sh4 = input()
            sh4 = int(sh4)
            prod = anhadirShawarma(saborShawarma=individualesList[sh4][0])
            orden.append(prod)
            print("Cuarta shawarma añadida")
            # añadir Papas Nativas Familiar
            # añadir bebida 1 Litro
            temp = ["Papas Nativas Familiar"]
            orden.append(temp)
            temp = [adicionalesList[9]]
            orden.append(temp)
            orden.append(temp)

    elif inputTipoProd == "4":
        print(inputTextExtras)
        inputExtra = input()
        if inputExtra == "1":
            # evaluar caso / seleccionar un item de la lista, mostrar solo los que cumplen el requisito: que sea shawarma
            print("Shawarma con extra pollo (+50%)")
            # añadir extra
        elif inputExtra == "2":
            print("Se ha añadido una (1) chicha y papas nativas personales")
            # añadir chicha y papas personales
        elif inputExtra == "3":
            # evaluar caso / seleccionar un item de la lista, mostrar solo los que cumplen el requisito: que sea papa 
            print("Se ha añadido chorizo a las papas")
            # añadir chorizo a las papas, 
        else:
            print("Ha seleccionado un valor incorrecto")
    elif inputTipoProd == "5":
        print(inputTextAdicionales)
        inputAdicionales = input()
        if int(inputAdicionales):
            intInputAdic = int(inputAdicionales)
            if intInputAdic in range(8):
                print("Seleccione el producto para el adicional:\n")
                rOrden(orden)                # mostrar orden
                seleccion = input()
                seleccion = int(seleccion)
                orden[seleccion].append(adicionalesList[intInputAdic][0])
                print("Se ha añadido", adicionalesList[intInputAdic][0])
            elif intInputAdic < 12 & intInputAdic > 8:
                print("Se ha añadido", adicionalesList[intInputAdic][0])
        else:
            print("Ha introducido un valor incorrecto")
        '''if inputAdicionales == "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8":
            print("gg")
        elif inputAdicionales == "9" | "10" | "11":
            print("se ha añadido", adicionalesList[int(inputAdicionales)][0])
        else:
            print("Ha seleccionado un valor incorrecto")'''
    return "1"

def cTicket():
    ticket = list()
    cuenta = 0
    return ticket

def rTicket(ticket):
    print(ticket)
    for i in ticket:
        cuenta = cuenta + ticket[i][-1]
    print("La cuenta es: S/.", cuenta)

def uTicket(ticket, itemT):
    ticket.append(itemT)
    return "1"

def dTicket(ticket):
    ticket = list()                 #vaciar la lista    #del ticket
    print("Ticket eliminado")
    return 1

def cOrden():
    orden = list()
    return orden

def rOrden(orden):
    for i in range(len(orden)):
        print(str(i+1) + ".", orden[i])
    print(orden)

def uOrden(orden, itemO):
    orden.append(itemO)
    return 1

def dOrden(orden):
    orden = list()                  # vaciar la lista   #del orden
    print("Orden eliminada")
    return 1

def cItem(orden, prod):
    orden.append(prod)
    return 1

def rItem(item):
    print(item)
    return 1

def uItem(item, prop):
    item.append(prop)
    return 1

def dItem(lista, itemIndex):       # deberia ser el index del item en la lista
    lista.pop(itemIndex+1)      # asi, el método que se use debería ser lista.pop(index)
    print("Producto eliminado")