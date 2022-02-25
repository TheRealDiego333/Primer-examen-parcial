import numpy as np
import sys
from random import randint 
import psycopg2
print("Ejercicio #2.4")
conexion = psycopg2.connect(
	host = "localhost",
	port = "5432",
	user = "postgres",
	password = "lin_$$33",
	dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio1;"
INSERT = "INSERT INTO ejercicio1(mensaje,operacion) VALUES(%s,%s);"

dado1 
