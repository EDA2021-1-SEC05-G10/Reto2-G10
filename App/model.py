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


from math import inf
from typing import ItemsView
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
    catalog= {'years': None, 'adquiyears': None, 'artists': None, 'artworks': None, 'artists_name': None,'artworks_id':None, 'Nationality':None}
    catalog['years']= mp.newMap(2000, 4021, 'CHAINING', 0.5, comparar)
    catalog['adquiyears']=mp.newMap(1700, 3421, 'CHAINING',0.5, comparar)
    catalog['artists']=mp.newMap(2000, 4021, 'CHAINING', 0.5,comparar)
    catalog['artworks']=mp.newMap(2000, 4021,'CHAINING', 0.5, comparar)
    catalog['artists_name']=mp.newMap(2000, 4021,'CHAINING', 0.5, comparar)
    catalog['artworks_id']=mp.newMap(2000, 4021,'CHAINING', 0.5, comparar)
    catalog['Nationality']=mp.newMap(200, 421,'CHAINING', 0.5, comparar)
    
    

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

def add_adquiyears(infoyears, catalog):
    info= mp.get(catalog['adquiyears'], infoyears['DateAcquired'])
    if info is None:
        artwork= lt.newList('SINGLE_LINKED')
        lt.addLast(artwork, infoyears)
        mp.put(catalog['adquiyears'],infoyears['DateAcquired'],artwork)
    else:
        lt.addLast(info['value'],infoyears)

def add_artists(infoartists, catalog):
    info= mp.get(catalog['artists'], infoartists['ConstituentID'])
    if info is None:
        mp.put(catalog['artists'],infoartists['ConstituentID'],infoartists)

def add_artworks(infoartworks, catalog):
    idartist= infoartworks['ConstituentID'][1: len(infoartworks['ConstituentID'])-1]
    llaves= idartist.split(', ')
    for lla in llaves:
        info= mp.get(catalog['artworks'], lla)
        if info is None:
            Artwork= lt.newList('SINGLE_LINKED')
            lt.addLast(Artwork, infoartworks)
            mp.put(catalog['artworks'], lla, Artwork)
        else:
            lt.addLast(info['value'], infoartworks)

def add_artists_Name(infoartists, catalog):
    info= mp.get(catalog['artists_name'], infoartists['DisplayName'])
    if info is None:
        mp.put(catalog['artists_name'],infoartists['DisplayName'],infoartists)

def add_artworks_id(infoartworksid, catalog):
    info= mp.get(catalog['artworks_id'], infoartworksid['ObjectID'])
    if info is None:
        mp.put(catalog['artworks_id'],infoartworksid['ObjectID'],infoartworksid)

def add_nacionality(infoartworks, catalog):
    idartist= infoartworks['ConstituentID'][1: len(infoartworks['ConstituentID'])-1]
    llaves= idartist.split(', ')
    for lla in llaves:
        info= mp.get(catalog['artists'], lla)['value']['Nationality']
        info1= mp.get(catalog['Nationality'], info)
        if info1 is None:
            Artwork= lt.newList('SINGLE_LINKED')
            lt.addLast(Artwork, infoartworks)
            mp.put(catalog['Nationality'], info, Artwork)
        else:
            lt.addLast(info1['value'], infoartworks)


# Funciones de consulta
def requerimiento1(catalog, fecha_inicial, fecha_final):
    llaves= mp.keySet(catalog['years'])
    lista = lt.newList()
    iterator1= it.newIterator(llaves)
    while it.hasNext(iterator1):
        elemento= it.next(iterator1)
        if elemento <= fecha_final and elemento >= fecha_inicial:
            info= mp.get(catalog['years'], elemento)['value']
            iterator2 = it.newIterator(info)
            while it.hasNext(iterator2):
                element = it.next(iterator2)
                lt.addLast(lista, element)
        
    
    return lista

def requerimiento2(catalog, fecha_inicial, fecha_final):
    llaves= mp.keySet(catalog['adquiyears'])
    lista = lt.newList()
    iterator1= it.newIterator(llaves)
    while it.hasNext(iterator1):
        elemento= it.next(iterator1)
        if elemento <= fecha_final and elemento >= fecha_inicial:
            info= mp.get(catalog['adquiyears'], elemento)['value']
            iterator2 = it.newIterator(info)
            while it.hasNext(iterator2):
                element = it.next(iterator2)
                lt.addLast(lista, element)
        
    
    return lista

def requerimiento3(catalog, Artist):
    idartista= mp.get(catalog['artists_name'],Artist)['value']['ConstituentID']
    infoobras= mp.get(catalog['artworks'], idartista)['value']
    infomedios=mp.newMap(200, 421,'CHAINING', 0.5, comparar)
    iterator1= it.newIterator(infoobras)
    while it.hasNext(iterator1):
        elemento= it.next(iterator1)
        info=mp.get(infomedios, elemento['Medium'])
        if info is None:
            medio= lt.newList('SINGLE_LINKED')
            lt.addLast(medio, elemento)
            mp.put(infomedios, elemento['Medium'], medio)
        else:
            lt.addLast(info['value'],elemento)
    llaves= mp.keySet(infomedios)
    llave_win=''
    comparador=0
    iterator2= it.newIterator(llaves)
    while it.hasNext(iterator2):
        elemento= it.next(iterator2)
        info=mp.get(infomedios, elemento)['value']
        if lt.size(info) > comparador:
            comparador= lt.size(info)
            llave_win = elemento
    rta=mp.get(infomedios, llave_win)['value']

    return [infoobras, llaves, rta]

def requerimiento4(catalog):
    lista= lt.newList('SINGLE_LINKED')
    llaves= mp.keySet(catalog['Nationality'])
    iterator1= it.newIterator(llaves)
    while it.hasNext(iterator1):
        elemento= it.next(iterator1)
        info= mp.get(catalog['Nationality'],elemento)
        if lt.size(lista) == 0:
            lt.addLast(lista, info)
        else:
            i=0
            j=lt.size(lista)+1
            while i < j:
                if lt.size((lt.getElement(lista, i))['value']) < lt.size(info['value']):
                    lt.insertElement(lista, (lt.getElement(lista, i)), i+1)
                    lt.insertElement(lista,info,i)
                    break
                elif i == lt.size(lista):
                    lt.insertElement(lista,info,i)
                                        
                i += 1
    return lista


def obteneratista(catalog, idartists):
    info= mp.get(catalog['artists'], idartists)
    if info is not None:
        return info['value']

def obtenerobras(catalog, idobras):
    info= mp.get(catalog['artworks'], idobras)
    if info is not None:
        return info['value']



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def comparar(Fecha1, Fecha2 ):
    if Fecha1 < (Fecha2['key']):
        return -1
    elif Fecha2['key'] < (Fecha1):
        return 1
    else:
        return 0

