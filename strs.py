import listas

listasTiposList = listas.listasTiposList
tipoProdList = listas.tipoProdList
individualesList = listas.individualesList
combosPersonalesList = listas.combosPersonalesList
combos2MasList = listas.combos2MasList
extrasList = listas.extrasList
adicionalesList = listas.adicionalesList

inputTextTipoProd = "Seleccione el tipo de producto:"               # tipoProdList
for i in range(len(tipoProdList)):
    inputTextTipoProd = inputTextTipoProd + "\n" + (str(i+1)) + ". " + tipoProdList[i]
#print(inputTextTipoProd)
'''
Seleccione el tipo de producto:
1. Individuales
2. Combos personales
3. Combos +2
4. Extras
5. Adicionales
'''

inputTextInvividuales = "Seleccione la shawarma:"                   # individualesList
for i in range(len(individualesList)):
    inputTextInvividuales = inputTextInvividuales + "\n" + str((i+1))+ ". " + individualesList[i][0]
#print(inputTextInvividuales)
'''
Seleccione la shawarma:
1. Chanqawarma
2. Dusiwarma
3. Pachawarma
4. Intiwarma
5. Charapawarma
6. Taypawarma
'''

inputTextCombosPersonales = "Seleccione el combo personal:"         # combosPersonalesList
for i in range(len(combosPersonalesList)):
    inputTextCombosPersonales = inputTextCombosPersonales + "\n" + (str(i+1)) + ". " + combosPersonalesList[i][0]
#print(inputTextCombosPersonales)
'''
Seleccione el combo personal:
1. Combo Chanqa
2. Combo Dusi
3. Combo Pacha
4. Combo Inti
5. Combo Charapa
6. Combo Taypa
'''

inputTextCombos2Mas = "Seleccione la promo:"                        # combos2MasList
for i in range(len(combos2MasList)):
    inputTextCombos2Mas = inputTextCombos2Mas + "\n" + (str(i+1)) + ". " + combos2MasList[i][0]
#print(inputTextCombos2Mas)
'''
Seleccione la promo:
1. Combo Duo
2. Combo Dupla
3. Combo Trío
4. Combo Familia
'''

inputTextAdicionales = "Seleccione el adicional:"                   # adicionalesList
for i in range(len(adicionalesList)):
    inputTextAdicionales = inputTextAdicionales + "\n" + (str(i+1)) + ". " + adicionalesList[i][0]
#print(inputTextAdicionales)
'''
Seleccione el adicional:
1. Jamón
2. Queso
3. Huevo
4. BBQ
5. Chorizo
6. Tocino
7. Cecina
8. Papas Nativas
9. Malta/Colita
10. Gaseosa
11. Chicha
'''

inputTextExtras = "Seleccione el extra:"                            # extrasList
for i in range(len(extrasList)):
    inputTextExtras = inputTextExtras + "\n" + (str(i+1)) + ". " + extrasList[i][0]
#print(inputTextExtras)
'''
Seleccione el extra:
1. Pollo adicional (+50%)
2. Papas + Chicha
3. Chorizo en Papas Nativas
'''