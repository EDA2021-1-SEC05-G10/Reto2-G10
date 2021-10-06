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

catalog = None

def requerimiento1(catalog,fecha_inicial, fecha_final):
    reque1= controller.requerimiento1(catalog,fecha_inicial, fecha_final) 
    print(lt.size(reque1))
    i=0
    j=lt.size(reque1)-4
    x=0
    iterator1= it.newIterator(reque1)
    print(reque1)
    while it.hasNext(iterator1) and i < 3:
        elemento= it.next(iterator1)
        
        print("Nombre del artista: " + (elemento['DisplayName']) 
        + "Año de Nacimiento: " + str(elemento['BeginDate']) + "Año de fallecimiento: " + str(elemento['EndDate']) 
        + "Nacionalidad: " +str(elemento['Nationality']) + "Genero: " +str(elemento['Gender']))
        i += 1
    iterator2= it.newIterator(reque1)
    while it.hasNext(iterator2) and x < lt.size(reque1):
        elemento=it.next(iterator2)
        if x >= j:
            print("Nombre del artista: " + str(elemento['DisplayName']) 
            + "Año de Nacimiento: " + str(elemento['BeginDate']) + "Año de fallecimiento: " + str(elemento['EndDate']) 
            + "Nacionalidad: " +str(elemento['Nationality']) + "Genero: " +str(elemento['Gender']))
        x += 1


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

    elif int(inputs[0]) == 2:
        requerimiento1(catalog, input("Ingresar Fecha Inicial: "), input("Ingresar Fecha Final: "))

    else:
        sys.exit(0)
sys.exit(0)
