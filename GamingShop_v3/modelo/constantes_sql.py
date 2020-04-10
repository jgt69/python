'''

Created on 3 abr. 2020

'''
# -*- coding: utf-8 -*-

SQL_INSERT_ITEM = "INSERT INTO `tabla_perifericos` (`tipo`, `marca`, `modelo`, `gama`, `precio`) VALUES (%s, %s, %s, %s, %s);"
SQL_LIST_ITEMS = "SELECT * FROM tabla_perifericos ;"
SQL_LIST_NOID =  "SELECT tipo, marca, modelo, gama, precio FROM tabla_perifericos ;"
SQL_BORRAR_ITEM = "DELETE FROM tabla_perifericos WHERE id = %s ;"
SQL_OBTENER_ITEM_POR_ID = "SELECT * FROM tabla_perifericos WHERE id = %s ;"
SQL_GUARDAR_CAMBIOS_ITEM = "UPDATE tabla_perifericos SET tipo = %s , marca = %s , modelo = %s, gama = %s, precio = %s WHERE id = %s ;"