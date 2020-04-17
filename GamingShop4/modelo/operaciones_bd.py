'''

Created on 3 abr. 2020

'''
# -*- coding: utf-8 -*-


import mysql.connector

from modelo import constantes_sql
from modelo.clases import Periferico



def conectar():
    mydb = mysql.connector.connect(

        host="localhost",
        user="root",
        database="bd_gaming_shop"

    )
    return mydb


# metodo que recibe un objeto de la clase Periferico()
def registro_periferico(producto):
    sql = constantes_sql.SQL_INSERT_ITEM

    mydb = conectar()

    cursor = mydb.cursor()
    # mirando el orden del insert formamos la tupla para insertar los datos
    val = (producto.tipo, producto.marca, producto.modelo, producto.gama, float(producto.precio), producto.soporte)

    try:
        cursor.execute(sql, val)
    except Exception as e:
        print(e)

    mydb.commit()

    id_info = cursor.lastrowid
    # desconectamos despues del commit
    mydb.disconnect()
    return id_info


def obtener_listado():

    sql = constantes_sql.SQL_LIST_ITEMS
    
    mydb = conectar()

    cursor = mydb.cursor()

    cursor.execute(sql)

    # transforma el resultado de la select sobre la BBDD en forma de lista
    resultado_lista = cursor.fetchall()

    mydb.disconnect()

    return resultado_lista


def obtener_listado_noid():

    sql = constantes_sql.SQL_LIST_NOID
    
    mydb = conectar()

    cursor = mydb.cursor()

    cursor.execute(sql)

    # transforma el resultado de la select sobre la BBDD en forma de lista
    resultado_lista = cursor.fetchall()

    mydb.disconnect()

    return resultado_lista


def borrar_item(index):
    sql = constantes_sql.SQL_BORRAR_ITEM
    mydb = conectar()
    cursor = mydb.cursor()
    val = (index, )
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()


def obtener_item_por_id(index):
    sql = constantes_sql.SQL_OBTENER_ITEM_POR_ID
    mydb = conectar()
    cursor = mydb.cursor()
    val = (index, )
    cursor.execute(sql, val)
    item_obtenido = cursor.fetchone()
    mydb.disconnect()
    objeto_periferico = Periferico(id = item_obtenido[0], tipo = item_obtenido[1], marca = item_obtenido[2],
                                   modelo = item_obtenido[3], gama = item_obtenido[4], precio = item_obtenido[5],
                                   soporte = item_obtenido[6])
    return objeto_periferico    


def guardar_cambios_producto(item):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_ITEM
    mydb = conectar()
    cursor = mydb.cursor()
    val = (item.tipo, item.marca, item.modelo, item.gama, float(item.precio), item.soporte, item.id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.disconnect()
