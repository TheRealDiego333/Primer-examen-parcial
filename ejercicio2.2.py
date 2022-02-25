import psycopg2
print("Ejercicio #2.2")
conexion = psycopg2.connect(
	host = "localhost",
	port = "5432",
	user = "postgres",
	password = "lin_$$33",
	dbname = "examen1"
)

SQL = "SELECT * FROM ejercicio2;"
INSERT = "INSERT INTO ejercicio2(angulo1,angulo2,angulo3) VALUES(%s,%s,%s);"

while (True):
	try:
		a1=float(input("Ingrese el primer angulo: "))
		a2=float(input("Ingrese el segundo angulo: "))
	except ValueError:
		print("Entrada invalida")
	if 0< a1 < 180 and 0<a2 <180:
		try:
			a3=180-a1-a2
			print("el tercer angulo es: ",a3)
			cursor = conexion.cursor()
			cursor.execute (INSERT,(a1,a2,a3))
			conexion.commit()
		except NameError:
			print("Ingrese un numero")	
		m = input("Quieres ver el historial de datos?(y/n): ")
		if m == 'y' or m == 'Y':
			cursor = conexion.cursor()
			cursor.execute(SQL)
			all_values = cursor.fetchall()
			print('Historial: ',  all_values)
	else:
		print("Angulos invalidos")

