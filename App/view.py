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
    print("0- Salir")

catalog = None

def requerimiento1(catalog,fecha_inicial, fecha_final):
    reque1= controller.requerimiento1(catalog,fecha_inicial, fecha_final) 
    print(lt.size(reque1))
    i=0
    j=lt.size(reque1)-3
    x=0
    iterator1= it.newIterator(reque1)
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        print(" Nombre del artista: " + (elemento['DisplayName']) 
        + " Año de Nacimiento: " + str(elemento['BeginDate']) + "\n Año de fallecimiento: " + str(elemento['EndDate']) 
        + " Nacionalidad: " +str(elemento['Nationality']) + "\n Genero: " +str(elemento['Gender']))
        i += 1
    iterator2= it.newIterator(reque1)
    while it.hasNext(iterator2) and x < lt.size(reque1):
        elemento=it.next(iterator2)
        if x >= j:
            print(" Nombre del artista: " + str(elemento['DisplayName']) 
            + " Año de Nacimiento: " + str(elemento['BeginDate']) + "\n Año de fallecimiento: " + str(elemento['EndDate']) 
            + " Nacionalidad: " +str(elemento['Nationality']) + "\n Genero: " +str(elemento['Gender']))
        x += 1

def requerimiento2(catalog,fecha_inicial, fecha_final):
    reque2= controller.requerimiento2(catalog,fecha_inicial, fecha_final) 
    print(lt.size(reque2))
    i=0
    j=lt.size(reque2)-3
    x=0
    comprados= 0
    iterator1= it.newIterator(reque2)
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        print(" Titulo: " + (elemento['Title']) 
        + " Arstista(s): " + obtenerArtistas(catalog, elemento['ConstituentID']) + "\n Fecha: " + str(elemento['Date']) 
        + " Medio: " +str(elemento['Medium']) + "\n Dimensiones: " +str(elemento['Dimensions']))
        i += 1
    iterator2= it.newIterator(reque2)
    while it.hasNext(iterator2) and x < lt.size(reque2):
        elemento=it.next(iterator2)
        if elemento['CreditLine'] == 'Purchase':
            comprados += 1
        if x >= j:
            print(" Titulo: " + (elemento['Title']) 
            + " Arstista(s): " + obtenerArtistas(catalog, elemento['ConstituentID']) + "\n Fecha: " + str(elemento['Date']) 
            + " Medio: " +str(elemento['Medium']) + "\n Dimensiones: " +str(elemento['Dimensions']))
        x += 1
    print('La cantidad de comprados es: ' + str(comprados))

def requerimiento3(catalog,Artist):
    reque3= controller.requerimiento3(catalog, Artist)
    print('El Artista tiene: '+ str(lt.size(reque3[0]))+' Obras.')
    print('El Artista utiliza: '+ str(lt.size(reque3[1]))+' Tecnicas.')
    iterator1= it.newIterator(reque3[2])
    i=0
    j=lt.size(reque3[2])-3
    x=0
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        print(" Titulo: " + (elemento['Title']) 
        + " Arstista(s): " + obtenerArtistas(catalog, elemento['ConstituentID']) + "\n Fecha: " + str(elemento['Date']) 
        + " Medio: " +str(elemento['Medium']) + "\n Dimensiones: " +str(elemento['Dimensions']))
        i += 1
    iterator2= it.newIterator(reque3[2])
    while it.hasNext(iterator2) and x < lt.size(reque3[2]):
        elemento=it.next(iterator2)
        if x >= j:
            print(" Titulo: " + (elemento['Title']) 
            + " Arstista(s): " + obtenerArtistas(catalog, elemento['ConstituentID']) + "\n Fecha: " + str(elemento['Date']) 
            + " Medio: " +str(elemento['Medium']) + "\n Dimensiones: " +str(elemento['Dimensions']))
        x += 1

def requerimiento4(catalog):
    reque4 = controller.requerimiento4(catalog)
    for i in range(1,10):
        elemento=lt.getElement(reque4,i)
        size = lt.size(elemento['value'])
        if elemento['key']=='':
            print('El pais: artistas de nacionalidad desconocida con: ' + str(size))
        else:
            print('El pais: ' + elemento['key'] + ' con: ' + str(size))
    peliculas= lt.getElement(reque4,1)['value']
    i=0
    j=lt.size(peliculas)-3
    x=0
    iterator1= it.newIterator(peliculas)
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        print(" Titulo: " + (elemento['Title']) 
        + " Arstista(s): " + obtenerArtistas(catalog, elemento['ConstituentID']) + "\n Fecha: " + str(elemento['Date']) 
        + " Medio: " +str(elemento['Medium']) + "\n Dimensiones: " +str(elemento['Dimensions']))
        i += 1
    iterator2= it.newIterator(peliculas)
    while it.hasNext(iterator2) and x < lt.size(peliculas):
        elemento=it.next(iterator2)
        if x >= j:
            print(" Titulo: " + (elemento['Title']) 
            + " Arstista(s): " + obtenerArtistas(catalog, elemento['ConstituentID']) + "\n Fecha: " + str(elemento['Date']) 
            + " Medio: " +str(elemento['Medium']) + "\n Dimensiones: " +str(elemento['Dimensions']))
        x += 1

def requerimiento5(catalog, Department):
    reque5= controller.requerimiento5(catalog, Department)
    lista_antiguos= reque5[0]
    lista_costosos= reque5[1]
    valor=reque5[2]
    peso= reque5[3]
    total_obras= reque5[4]
    print('Total de obras para transportar es: '+str(total_obras))
    print('El valor total para transportar es: '+str(valor))
    print('El peso total para transportar es: '+str(peso))
    for i in range(1,5):
        elemento= lt.getElement(lista_antiguos,i)
        valor2=0.00
        if elemento['Weight (kg)'] == '':
            valor2= 48.00
        else:
            valor2= float(elemento['Weight (kg)']) *72.00
        print(" Titulo: " + (elemento['Title']) 
            + " Arstista(s): " + obtenerArtistas(catalog, elemento['ConstituentID'])+" Clasificacion: "+str(elemento['Classification']) + "\n Fecha: " + str(elemento['Date']) 
            + " Medio: " +str(elemento['Medium']) + "\n Dimensiones: " +str(elemento['Dimensions'])+ " Costo de Transporte: "+str(valor2)+ "\n") 
    
    for i in range(1,5):
        elemento= lt.getElement(lista_costosos,i)
        valor2=0.00
        if elemento['Weight (kg)'] == '':
            valor2= 48.00
        else:
            valor2= float(elemento['Weight (kg)']) *72.00
        print(" Titulo: " + (elemento['Title']) 
            + " Arstista(s): " + obtenerArtistas(catalog, elemento['ConstituentID'])+" Clasificacion: "+str(elemento['Classification']) + "\n Fecha: " + str(elemento['Date']) 
            + " Medio: " +str(elemento['Medium']) + "\n Dimensiones: " +str(elemento['Dimensions'])+ " Costo de Transporte: "+str(valor2) + "\n")



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
    

    else:
        sys.exit(0)
sys.exit(0)
