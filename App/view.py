"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """




import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import linkedlistiterator as it
assert cf
import time 
from prettytable import PrettyTable

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1")
    print("3- Requerimiento 2")
    print("4- Requerimiento 3")
    print("5- Requerimiento 4")
    print("6- Requerimiento 5")
    print("7- Requerimiento 6")
    print("0- Salir")

catalog = None

def requerimiento1(catalog,fecha_inicial, fecha_final):
    inicio = time.time()
    reque1= controller.requerimiento1(catalog,fecha_inicial, fecha_final) 
    print(lt.size(reque1))
    i=0
    j=lt.size(reque1)-3
    x=0
    tabla = PrettyTable()
    tabla.field_names = ["Nombre", "Nacimiento", "Fallecimiento", "Nacionalidad","Genero"]  
    tabla._max_width={"Nombre":40,"Nacimiento":14,"Fallecimiento":14, "Nacionalidad":17, "Genero":17}  
    iterator1= it.newIterator(reque1)
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        datos = elemento['DisplayName'],elemento['BeginDate'],str(elemento['EndDate']),elemento['Nationality'],str(elemento['Gender'])
        tabla.add_row(datos)
        i += 1
    iterator2= it.newIterator(reque1)
    while it.hasNext(iterator2) and x < lt.size(reque1):
        elemento=it.next(iterator2)
        if x >= j:
            datos = elemento['DisplayName'],elemento['BeginDate'],str(elemento['EndDate']),elemento['Nationality'],str(elemento['Gender'])
            tabla.add_row(datos)
        x += 1
    print(tabla)
    fin = time.time()
    print(fin-inicio)

def requerimiento2(catalog,fecha_inicial, fecha_final):
    inicio = time.time()
    reque2= controller.requerimiento2(catalog,fecha_inicial, fecha_final) 
    print(lt.size(reque2))
    tabla = PrettyTable()
    tabla.field_names = ["Titulo", "Artista(s)", "Fecha", "Medio","Dimensiones"]  
    tabla._max_width={"Titulo":25,"Artista(s)":20,"Fecha":17, "Medio":17, "Dimensiones":20}
    i=0
    j=lt.size(reque2)-3
    x=0
    comprados= 0
    iterator1= it.newIterator(reque2)
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        datos = elemento['Title'],obtenerArtistas(catalog, elemento['ConstituentID']),str(elemento['Date']),str(elemento['Medium']),str(elemento['Dimensions'])
        tabla.add_row(datos)
        i += 1
    iterator2= it.newIterator(reque2)
    while it.hasNext(iterator2) and x < lt.size(reque2):
        elemento=it.next(iterator2)
        if elemento['CreditLine'] == 'Purchase':
            comprados += 1
        if x >= j:
            artista = obtenerArtistas(catalog, elemento['ConstituentID'])
            datos = elemento['Title'],artista,str(elemento['Date']),str(elemento['Medium']),str(elemento['Dimensions'])
            tabla.add_row(datos)
        x += 1
    print(tabla)
    print('La cantidad de comprados es: ' + str(comprados))
    fin = time.time()
    print(fin-inicio)

def requerimiento3(catalog,Artist):
    inicio = time.time()
    reque3= controller.requerimiento3(catalog, Artist)
    print('El Artista tiene: '+ str(lt.size(reque3[0]))+' Obras.')
    print('El Artista utiliza: '+ str(lt.size(reque3[1]))+' Tecnicas.')
    tabla = PrettyTable()
    tabla.field_names = ["Titulo", "Artista(s)", "Fecha", "Medio","Dimensiones"]  
    tabla._max_width={"Titulo":25,"Artista(s)":20,"Fecha":17, "Medio":17, "Dimensiones":20}
    iterator1= it.newIterator(reque3[2])
    i=0
    j=lt.size(reque3[2])-3
    x=0
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        datos = elemento['Title'],obtenerArtistas(catalog, elemento['ConstituentID']),str(elemento['Date']),str(elemento['Medium']),str(elemento['Dimensions'])
        tabla.add_row(datos)
        i += 1
    iterator2= it.newIterator(reque3[2])
    while it.hasNext(iterator2) and x < lt.size(reque3[2]):
        elemento=it.next(iterator2)
        if x >= j:
            datos = elemento['Title'],obtenerArtistas(catalog, elemento['ConstituentID']),str(elemento['Date']),str(elemento['Medium']),str(elemento['Dimensions'])
            tabla.add_row(datos)
        x += 1
    print(tabla)
    fin = time.time()
    print(fin-inicio)

def requerimiento4(catalog):
    inicio = time.time()
    reque4 = controller.requerimiento4(catalog)
    tabla1 = PrettyTable()
    tabla1.field_names = ["País", "# de obras"]  
    for i in range(1,10):
        elemento=lt.getElement(reque4,i)
        size = lt.size(elemento['value'])
        if elemento['key']=='':
            datos='nacionalidad desconocida', str(size)
            tabla1.add_row(datos)
        else:
            datos = elemento["key"],str(size)
            tabla1.add_row(datos)
    print(tabla1)
    peliculas= lt.getElement(reque4,1)['value']
    i=0
    j=lt.size(peliculas)-3
    x=0
    iterator1= it.newIterator(peliculas)
    tabla2 = PrettyTable()
    tabla2.field_names = ["Titulo", "Artista(s)","Fecha","Medio","Dimensiones"] 
    tabla2._max_width={"Titulo":25,"Artista(s)":20,"Fecha":17, "Medio":17, "Dimensiones":15}
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        datos=elemento['Title'], obtenerArtistas(catalog, elemento['ConstituentID']),str(elemento['Date']), str(elemento['Medium']),str(elemento['Dimensions'])
        tabla2.add_row(datos)
        i += 1
    iterator2= it.newIterator(peliculas)
    while it.hasNext(iterator2) and x < lt.size(peliculas):
        elemento=it.next(iterator2)
        if x >= j:
            datos=elemento['Title'], obtenerArtistas(catalog, elemento['ConstituentID']),str(elemento['Date']), str(elemento['Medium']),str(elemento['Dimensions'])
            tabla2.add_row(datos)
        x += 1
    print(tabla2)
    fin = time.time()
    print(fin-inicio)


def requerimiento5(catalog, Department):
    inicio = time.time()
    reque5= controller.requerimiento5(catalog, Department)
    tabla1 = PrettyTable()
    tabla1.field_names = ["Titulo", "Artista(s)","Classification","Fecha","medio","Dimensiones","Valor"] 
    tabla1._max_width={"Titulo":15,"Artista(s)":15,"Classification":17, "Fecha":15,"medio":15, "Dimensiones":15,"Valor":10}
    lista_antiguos= reque5[0]
    lista_costosos= reque5[1]
    valor=reque5[2]
    peso= reque5[3]
    total_obras= reque5[4]
    print('Total de obras para transportar es: '+str(total_obras))
    print('El valor total para transportar es: '+str(valor))
    print('El peso total para transportar es: '+str(peso))
    for i in range(1,6):
        elemento= lt.getElement(lista_antiguos,i)
        valor2=0.00
        if obtenermetraje(elemento) == 0:
            valor2= 48.00
        else:
            valor2= obtenermetraje(elemento) *72.00
            
        x =((elemento['Title']),obtenerArtistas(catalog, elemento['ConstituentID']),str(elemento['Classification']),str(elemento['Date']), 
            str(elemento['Medium']),str(elemento['Dimensions']),str(valor2)) 
        tabla1.add_row(x)
    tabla2 = PrettyTable()
    tabla2.field_names = ["Titulo", "Artista(s)","Classification","Fecha","medio","Dimensiones","Valor"] 
    tabla2._max_width={"Titulo":15,"Artista(s)":15,"Classification":17, "Fecha":15,"medio":15, "Dimensiones":15,"Valor":10}
    for i in range(1,6):
        elemento= lt.getElement(lista_costosos,i)
        valor2=0.00
        if obtenermetraje(elemento) == 0:
            valor2= 48.00
        else:
            valor2= obtenermetraje(elemento) *72.00
        x =((elemento['Title']),obtenerArtistas(catalog, elemento['ConstituentID']),str(elemento['Classification']),str(elemento['Date']), 
            str(elemento['Medium']),str(elemento['Dimensions']),str(valor2)) 
        tabla2.add_row(x)
    print(tabla2,tabla1)
    fin = time.time()
    print(fin-inicio)
def obtenermetraje(elemento):
    costoi= elemento['Dimensions']
    whe=costoi.split('(')
    if len(whe)>1:
        weight=whe[len(whe)-1]
        if len(weight.split(' '))>2:
            med1=weight.split(' ')[0]
            med2=weight.split(' ')[2]
            casoe=med2.split('c')
            if len(casoe)>1:
                med2=casoe[0]
            try:    
                pesoAct= (float(med1)*float(med2))/10000
            except:
                pesoAct=0.0
            return pesoAct
        else:
            return (float(weight.split(' ')[0])*1)/10000
    else:
        return 0

def requerimiento6(catalog, cant, fechaInicio, fechaFinal):
    inicio = time.time()
    x,Artw = controller.requerimiento6(catalog, cant, fechaInicio, fechaFinal)  
    tablaPro = PrettyTable()
    tablaPro.field_names = ["id", "Nombre","Fecha nacimiento","Genero","Bio artista","Wiki QID","Cant obras"] 
    tablaPro._max_width={"id":15,"Nombre":20,"Fecha nacimiento":17, "Genero":17, "Bio artista":18,"Wiki QID":18,"Cant obras":5}
    tablaArtw = PrettyTable()
    tablaArtw.field_names = ["ObjectID","Title","Medium","Date","DateAcquired","Department","Classification"]
    tablaArtw._max_width={"ObjectID":15,"Title":15,"Medium":15, "Date":17, "DateAcquired":20,"Department":20,"Classification":20}
    for cada in x:
        tablaPro.add_row(cada)
       
    idx = 0
    iterator1= it.newIterator(Artw)    
    while idx <5 and it.hasNext(iterator1):
        cada= it.next(iterator1)
        datos = [cada["ObjectID"],cada["Title"],cada["Medium"],cada["Date"],cada["DateAcquired"],cada["Department"],cada["Classification"]]
        tablaArtw.add_row(datos)
        idx+=1
    print(tablaPro.get_string(sortby="Cant obras",reversesort=True))
    print(tablaArtw)
    fin = time.time()
    print(fin-inicio)

def obtenerArtistas(catalog, idartists):
    idartist= idartists[1: len(idartists)-1]
    llaves= idartist.split(', ')
    rta= ''
    for lla in llaves:
        rta += ((controller.obtenerartista(catalog, lla)['DisplayName'])+ ' , ')
        
    return rta

def obtenerObras(catalog, idartworks):
    idartworks= idartworks[1: len(idartworks)-1]
    llaves= idartworks.split(', ')
    rta= ''
    for lla in llaves:
        rta += ((controller.obtenerobras(catalog, lla)['DisplayName'])+ ' , ')
        
    return rta


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog= controller.initCatalog()

        controller.loadDataArtists(catalog)
        controller.loadDataArtworks(catalog)

    elif int(inputs[0]) == 2:
        requerimiento1(catalog, input("Ingresar Fecha Inicial: "), input("Ingresar Fecha Final: "))
    elif int(inputs[0]) == 3:
        requerimiento2(catalog, input("Ingresar Fecha Inicial(AAAA-MM-DD): "), input("Ingresar Fecha Final(AAAA-MM-DD): "))
    elif int(inputs[0]) == 4:
        requerimiento3(catalog, input("Ingresar Nombre del Artista: "))
    elif int(inputs[0]) == 5:
        requerimiento4(catalog)
    elif int(inputs[0]) == 6:
        requerimiento5(catalog, input("Ingresar Departamento: "))
    elif int(inputs[0]) == 7:
        requerimiento6(catalog, input("Ingresar cantidad de artistas: "),input("Ingresar la fecha de inicio: "),input("Ingresar la fecha final: ") )

    else:
        sys.exit(0)
sys.exit(0)
