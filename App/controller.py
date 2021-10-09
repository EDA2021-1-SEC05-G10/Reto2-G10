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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos
def loadDataArtists(catalog):
    artistsfile = cf.data_dir + "Moma/Artists-utf8-small.csv"
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.add_years(artist, catalog)
        model.add_artists(artist, catalog)
        model.add_artists_Name(artist, catalog)

def loadDataArtworks(catalog):
    artworksfile = cf.data_dir + "Moma/Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.add_adquiyears(artwork, catalog)
        model.add_artworks(artwork, catalog)
        model.add_artworks_id(artwork, catalog)
        model.add_nacionality(artwork, catalog)


# Funciones para la carga de datos


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def requerimiento1(catalog, fecha_inicial, fecha_final):

    return model.requerimiento1(catalog, fecha_inicial, fecha_final)

def requerimiento2(catalog, fecha_inicial, fecha_final):

    return model.requerimiento2(catalog, fecha_inicial, fecha_final)

def requerimiento3(catalog, Artist):
    return model.requerimiento3(catalog, Artist)

def requerimiento4(catalog):
    return model.requerimiento4(catalog)

def obtenerartista(catalog, llaves):

    return model.obteneratista(catalog, llaves)

def obtenerobras(catalog, llaves):

    return model.obtenerobra(catalog, llaves)