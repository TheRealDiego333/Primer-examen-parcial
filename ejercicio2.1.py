import numpy as np
import os
import psycopg2
print("Ejercicio #2.1")
conexion = psycopg2.connect(
	host = "localhost",
	port = "5432",
	user = "postgres",
	password = "lin_$$33",
	dbname = "examen1"
)

SQL = "SELECT * FROM ejercicio1;"
INSERT = "INSERT INTO ejercicio1(edad,cumpleaños,año,mes,dia) VALUES(%s,%s,%s,%s,%s);"
edad = 0
cump = ""
dhoy = 24
mhoy = 2
ahoy = 2022

while (True):
	try:
		dn = int(input("Ingrese el día en que nacio: "))
		mn = int(input("Ingrese el mes en que nacio: "))
		an = int(input("Ingrese el año en que nacio: "))
		edad = ahoy-an
		if mhoy < mn:
			cump= "Todavia no cumple años"
		elif mhoy > mn:
			cump = "Ya cumplio años"
		elif mhoy == mn:
			if dhoy<dn:
				cump = "Todavia no cumple años"
			elif dhoy>dn:
				cump = "Ya cumplio años"
			elif dhoy == dn:
				cump = "Cumple años hoy"
		print ("Cumple %d este año y %s\n"%(edad,cump))
		cursor = conexion.cursor()
		cursor.execute (INSERT,(edad,cump,an,mn,dn))
		conexion.commit()

	except ValueError:
		print ("Ingrese un valor valido")
	
	m = input("Quieres ver el historial de datos?(y/n): ")
	if m == 'y' or m == 'Y':
		cursor = conexion.cursor()
		cursor.execute(SQL)
		all_values = cursor.fetchall()
		print("Historial: ",  all_values)
