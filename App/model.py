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
    catalog= {'years': None, 'adquiyears': None, 'artists': None, 'artworks': None, 'artists_name': None,'artworks_id':None, 'Nationality':None, 'Department': None}
    catalog['years']= mp.newMap(2000, 4021, 'CHAINING', 0.5, comparar)
    catalog['adquiyears']=mp.newMap(1700, 3421, 'CHAINING',0.5, comparar)
    catalog['artists']=mp.newMap(2000, 4021, 'CHAINING', 0.5,comparar)
    catalog['artworks']=mp.newMap(2000, 4021,'CHAINING', 0.5, comparar)
    catalog['artists_name']=mp.newMap(2000, 4021,'CHAINING', 0.5, comparar)
    catalog['artworks_id']=mp.newMap(2000, 4021,'CHAINING', 0.5, comparar)
    catalog['Nationality']=mp.newMap(200, 421,'CHAINING', 0.5, comparar)
    catalog['Department']=mp.newMap(2000, 421,'CHAINING', 0.5, comparar )
    
    

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

def add_department(artwork,catalog):
    infodepartment= artwork['Department']
    info= mp.get(catalog['Department'],infodepartment)
    if info is None:
        lista= lt.newList('SINGLE_LINKED')
        lt.addLast(lista, artwork )
        mp.put(catalog['Department'],infodepartment,lista)
    else:
        lt.addLast(info['value'], artwork )


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
    lista = sortBegin(lista)
    
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
            lt.insertElement(lista, info,1)
        else:
            i=1
            j=lt.size(lista)
            while i <= j:
                tamaño_actual = lt.size((lt.getElement(lista, i))['value'])
                tamaño_nuevo = lt.size(info['value'])
                if  tamaño_actual < tamaño_nuevo :
                    elemento_actual =lt.getElement(lista, i)
                    elemento_nuevo=info
                    lt.deleteElement(lista,i)
                    lt.insertElement(lista,elemento_nuevo,i)
                    lt.insertElement(lista,elemento_actual,i+1)
                    break
                elif i == lt.size(lista):
                    lt.insertElement(lista,info,i+1)
                                        
                i += 1
    return lista
def requerimiento5(catalog, Department):
    obrasantiguas=lt.newList('SINGLE_LINKED')
    obrascostosas=lt.newList('SINGLE_LINKED')
    obras= mp.get(catalog['Department'], Department)['value']
    valor= 0.00
    peso= 0.00
    iterator1= it.newIterator(obras)
    while it.hasNext(iterator1):
        elemento= it.next(iterator1)
        if lt.size(obrasantiguas) != 0 and lt.size(obrascostosas) != 0:
            i=1
            j=lt.size(obrasantiguas)
            h=1
            k=lt.size(obrascostosas)
            while i <= j:
                fechai= lt.getElement(obrasantiguas, i)
                date=fechai['Date']
                if date != '' and date != ' ' and date is not None and elemento['Date']!='' and elemento['Date']!= ' ' and elemento['Date'] is not None:
                    if float(elemento['Date']) < float(date) :
                        viejo= lt.getElement(obrasantiguas, i)
                        lt.deleteElement(obrasantiguas, i)
                        lt.insertElement(obrasantiguas, elemento, i)
                        lt.insertElement(obrasantiguas,viejo,i+1)
                        break
                elif i == j:
                    lt.insertElement(obrasantiguas, elemento,i+1)
                i+=1
            while  h <= k:
                pesoAct=obtenermetraje(lt.getElement(obrascostosas, h))
                pesoNue=obtenermetraje(elemento)
                if pesoAct is not None:
                    if pesoNue > pesoAct :
                        maspesado= lt.getElement(obrascostosas, h)
                        lt.deleteElement(obrascostosas, h)
                        lt.insertElement(obrascostosas, elemento, h)
                        lt.insertElement(obrascostosas,maspesado,h+1)
                        break
                elif h == k:
                    lt.insertElement(obrascostosas, elemento,h+1)

                h+=1
        else:
            lt.addLast(obrasantiguas, elemento)
            lt.addLast(obrascostosas, elemento)

        if obtenermetraje == 0:
            valor += 48.00
        else:
            try:
                peso2= float(elemento['Weight (kg)'])
            except:
                peso2=0
            pes=obtenermetraje(elemento)
            valor2= pes * 72.00
            valor += valor2
            peso += peso2


    return [obrasantiguas, obrascostosas, valor, peso, lt.size(obras)]

def requerimiento6(catalog,cant,fechaInicio,fechaFinal):
    mpArt = catalog['artists']
    cantObras = mp.newMap(numelements=30,maptype="PROBING",loadfactor=0.7)
    ids = lt.newList()
    autores = lt.newList()
    x = mp.newMap(numelements=100,maptype="PROBING",loadfactor=0.7)
    for a in lt.iterator(mp.valueSet(mpArt)):
        if a["BeginDate"]>=fechaInicio and a["BeginDate"]<=fechaFinal:
            lt.addLast(ids,a["ConstituentID"])
            lt.addLast(autores,a)
    for cada in lt.iterator(ids):
        if mp.get(catalog["artworks"],cada) is not None:
            mp.put(x,lt.size(me.getValue(mp.get(catalog["artworks"],cada))),cada)
            
            mp.put(cantObras,lt.size(me.getValue(mp.get(catalog["artworks"],cada))),cada)
    
    lis = lt.newList(datastructure="SINGLE_LINKED")
    posi = 1
    while int(lt.size(lis))< int(cant):
        mayor = 1
        igual = 0
        for a in lt.iterator(mp.keySet(cantObras)):
            if int(a) > mayor:
                mayor = int(a)
        lt.insertElement(lis,mp.get(catalog["artworks"],me.getValue(mp.get(x,mayor))),posi)
        mp.remove(cantObras,mayor)
        posi+=1
    id = lt.firstElement(me.getValue(lt.firstElement(lis)))["ConstituentID"]
    id = id.replace("[","")
    id = id.replace("]","") 
    if mp.get(catalog["artworks"],id) is not None:
        Art = me.getValue(mp.get(catalog["artworks"],id))
        Art = sortAdq(Art)
    x=[]
    iterator1= it.newIterator(autores)
    while it.hasNext(iterator1):
        au= it.next(iterator1)       
        id = au["ConstituentID"]
        id = id.replace("[","")
        id = id.replace("]","") 
        if mp.get(catalog["artworks"],id) is not None:
            datos = [au["ConstituentID"],au["DisplayName"],au["BeginDate"],au["Gender"],au["ArtistBio"],au["Wiki QID"],lt.size(me.getValue(mp.get(catalog["artworks"],id)))]
            x.append(datos)
        
    return x,Art
    

def obteneratista(catalog, idartists):
    info= mp.get(catalog['artists'], idartists)
    if info is not None:
        return info['value']

def obtenerobras(catalog, idobras):
    info= mp.get(catalog['artworks'], idobras)
    if info is not None:
        return info['value']

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

# Funciones utilizadas para comparar elementos dentro de una lista
def compararAdq(fecha1,fecha2):
    return (fecha1['DateAcquired'] < fecha2['DateAcquired'])
def compareBegin(autor1,autor2):
    return (autor1['BeginDate'] < autor2['BeginDate'])
# Funciones de ordenamiento
def comparar(Fecha1, Fecha2 ):
    if Fecha1 < (Fecha2['key']):
        return -1
    elif Fecha2['key'] < (Fecha1):
        return 1
    else:
        return 0
def sortAdq(catalog):
    sorted_list = sa.sort(catalog, compararAdq)
    return sorted_list
def sortBegin(catalog):
    sorted_list = sa.sort(catalog, compareBegin)
    return sorted_list

