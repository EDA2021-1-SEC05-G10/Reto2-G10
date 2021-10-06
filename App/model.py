"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from typing import ItemsView
from DISClib.DataStructures.arraylist import iterator
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import DISClib.DataStructures.linkedlistiterator as it

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog= {'years': None}
    catalog['years']= mp.newMap(2000, 4021, 'CHAINING', 0.5, comparaFechas)
    

    return catalog


# Funciones para creacion de datos
def add_years(infoyears, catalog):
    info= mp.get(catalog['years'], infoyears['BeginDate'])
    if info is None:
        artists= lt.newList('SINGLE_LINKED')
        lt.addLast(artists, infoyears)
        mp.put(catalog['years'],infoyears['BeginDate'],artists)
    else:
        lt.addLast(info['value'],infoyears)
    


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta
def requerimiento1(catalog, fecha_inicial, fecha_final):
    llaves= mp.keySet(catalog['years'])
    i=0
    lista = lt.newList()
    iterator1= it.newIterator(llaves)
    while it.hasNext(iterator1):
        elemento= it.next(iterator1)
        if elemento <= fecha_final and elemento >= fecha_inicial:
            info= mp.get(catalog['years'], elemento)['value']
            for element in info:
                lt.addLast(lista, element)
        i += 1
    return lista
    


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def comparaFechas(Fecha1, Fecha2 ):
    if int(Fecha1) < int(Fecha2['key']):
        return -1
    elif int(Fecha2['key']) < int(Fecha1):
        return 1
    else:
        return 0

