import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #3")
conexion = psycopg2.connect(
	host = "localhost",
	port = "5432",
	user = "postgres",
	password = "lin_$$33",
	dbname = "examen1"
)

SQL = "SELECT * FROM ejercicio3;"
INSERT = "INSERT INTO ejercicio3(centenas,decenas,unidades) VALUES(%s,%s,%s);"

while(True):
	numero = int (input ('Ingresa el valor de numero: '))
	centenas=(numero%1000-numero%100)//100
	decenas=(numero%100-numero%10)//10
	unidades=numero%10
	print ("Valor de centenas: ", (centenas))
	print ("Valor de decenas: " , (decenas))
	print ("Valor de unidades: ",(unidades))
	print ()
	cursor = conexion.cursor()
	cursor.execute (INSERT,(centenas,decenas,unidades))
	conexion.commit()

	m = input("Quieres ver el historial de datos?(y/n): ")
	if m == 'y' or m == 'Y':
		cursor = conexion.cursor()
		cursor.execute(SQL)
		all_values = cursor.fetchall()
		print("Historial: ",  all_values)

 
