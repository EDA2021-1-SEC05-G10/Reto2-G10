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
    print("8- Laboratorio 6")
    print("0- Salir")

catalog = None

def requerimiento1(catalog,fecha_inicial, fecha_final):
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

def requerimiento2(catalog,fecha_inicial, fecha_final):
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

def requerimiento3(catalog,Artist):
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

def requerimiento4(catalog):
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
        x=controller.requerimiento5(catalog, input("Nombre del departamento a trasladar: "))
        print(x)
    elif int(inputs[0]) == 7:
        x=controller.requerimiento6(catalog, input("Cantidad de artistas: "),input("Fecha inicial: "),input("Fecha final: "))
        print(x)  
    elif int(inputs[0]) == 8:
        nac = input("nacionalidad: ")
        start_time = time.process_time()
        print(controller.labo6(catalog, nac))
        stop_time = time.process_time()
        tiempo = (stop_time-start_time)*1000
        print(tiempo)

    else:
        sys.exit(0)
sys.exit(0)
