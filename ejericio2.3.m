clc; clear all; close all;
pkg load database;
retry= true;
retry1= true;
retry2= true;
retry3= true;
while retry
      a1="0";
      fprintf("Ingrese un numero entre 1y 999 \n");
      a1=input("El numero: ","s");      
      c=a1(1);
      d=a1(2);
      u=a1(3);
      fprintf("Valor de centenas: %s \n", c)
      fprintf("Valor de decenas: %s \n" , d)
      fprintf("Valor de unidades: %s \n", u)
      params= cell(1,3);
      uu=str2double(u);
      dd=str2double(d);
      cc=str2double(c);
      params{1,1}= cc;
      params{1,2}= dd;
      params{1,3}= uu;

      conn = pq_connect(setdbopts('dbname','examen1','host','localhost',
      'port','5432','user','postgres','password','lin_$$33'));
      N=pq_exec_params(conn, "insert into ejercicio3(centenas, decenas, unidades) values($1,$2,$3);",params); %insertar datos en la tabla
      
	m=(input('Quiere ver historial?(y=1/n=2)'))
	if m == 1
		conn = pq_connect(setdbopts('dbname','examen1','host','localhost',
		'port','5432','user','postgres','password','lin_$$33'));
		N=pq_exec_params(conn, "Select * from ejercicio11;"); 
		disp(N)

	endif
endwhile
