import numpy as np
import sys
import random 
import psycopg2
print("Ejercicio #2.4")
conexion = psycopg2.connect(
	host = "localhost",
	port = "5432",
	user = "postgres",
	password = "lin_$$33",
	dbname = "examen1"
)

SQL = "SELECT * FROM ejercicio4;"
INSERT = "INSERT INTO ejercicio4(Dado1,Dado2,Resultado) VALUES(%s,%s,%s);"



while(True):
	d1=random.randint(1,6)
	print("Dado 1: ",d1)
	d2=random.randint(1,6)
	print("Dado 2: ",d2)
	suma = d1+d2
	if suma == 8:
		print("Ganaste!")
		cursor = conexion.cursor()
		cursor.execute (INSERT,(d1,d2,"Ganaste"))
		conexion.commit()
		h = input("Quieres ver el historial de datos?(y/n): ")
		if h == 'y' or h == 'Y':
			cursor = conexion.cursor()
			cursor.execute(SQL)
			all_values = cursor.fetchall()
			print("Historial: ",  all_values)

		m=input("Quieres continuar? (y/n)")
		if m == 'n' or m == 'N':
			break

	elif suma ==7:
		print("Perdiste")
		cursor = conexion.cursor()
		cursor.execute (INSERT,(d1,d2,"Perdiste"))
		conexion.commit()
		h = input("Quieres ver el historial de datos?(y/n): ")
		if h == 'y' or h == 'Y':
			cursor = conexion.cursor()
			cursor.execute(SQL)
			all_values = cursor.fetchall()
			print("Historial: ",  all_values)

		m=input("Quieres continuar? (y/n)")
		if m == 'n' or m == 'N':
			break

	else:
		cursor = conexion.cursor()
		cursor.execute (INSERT,(d1,d2," "))
		conexion.commit()
		h = input("Quieres ver el historial de datos?(y/n): ")
		if h == 'y' or h == 'Y':
			cursor = conexion.cursor()
			cursor.execute(SQL)
			all_values = cursor.fetchall()
			print("Historial: ",  all_values)

		m=input("Quieres continuar? (y/n)")
		if m == 'n' or m == 'N':
			break
