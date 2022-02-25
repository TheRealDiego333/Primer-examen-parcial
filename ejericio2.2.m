clc; clear all; close all;
pkg load database;
retry= true;
retry1= true;
retry2= true;
retry3= true;
while retry
          fprintf("Ingrese el primer angulo \n");
          a1=input("Angulo 1:   ");
          if a1>=180 || a1<=0
            fprintf("\nRevise el valor ingresado\n");
          else
            retry1=false;
          endif
      
          fprintf("Ingrese el segundo angulo \n");
          a2=input("Angulo 2:   ");
          if a2>180 || a2<=0 || a1+a2>1180
            fprintf("\nRevise el valor ingresado\n");
          else
            retry2=false;
          endif

      a3=180-a1-a2;
      fprintf("El Tercer Angulo es: %d \n ", a3);
      params= cell(1,3);
      params{1,1}=a1;
      params{1,2}=a2;
      params{1,3}=a3;
      conn = pq_connect(setdbopts('dbname','examen1','host','localhost',
      'port','5432','user','postgres','password','lin_$$33'));
      N=pq_exec_params(conn, "insert into ejercicio2(angulo1, angulo2, angulo3) values($1,$2,$3);",params); %insertar datos en la tabla
      
   

    m=(input('Quiere ver historial?(y=1/n=2)'))
    if m == 1
   	    conn = pq_connect(setdbopts('dbname','examen1','host','localhost',
	    'port','5432','user','postgres','password','lin_$$33'));
	    N=pq_exec_params(conn, "Select * from ejercicio11;"); 
	    disp(N)

    endif    
endwhile
