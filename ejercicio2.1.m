clc; clear all; close all;
pkg load database
retry= true;
cumple = '';
edad=0;
while retry
	dt=24;
	mt= 2;
	yt=2022;

	fprintf("Ingrese el dia en que nacio \n");
	dy=input("Dia:   ");
	fprintf("Ingrese el mes en que nacio \n");
	mon=input("Mes:   ");
	fprintf("Ingrese el año en que nacio \n");
	yr=input("Año:   ");

	if mt<mon
	cumple='No ha cumplido años';
	edad= yt-yr;
	elseif mt>mon
	cumple='Ya cumplio años';
	edad= yt-yr;
	elseif mt==mon
	if dt>dy
	  cumple='Ya cumplio años';
	  edad= yt-yr;
	elseif dt<dy
	  cumple='No ha cumplido años';
	  edad= yt-yr;
	elseif dt==dy
	  cumple='Hoy cumple años';
	  edad= yt-yr;
	endif
	endif

	fprintf("Esta persona cumple %d este año y %s\n ",edad,cumple );
	params= cell(1,5);
	params{1,1}=edad;
	params{1,2}=cumple;
	params{1,3}=yr;
	params{1,4}=mon;
	params{1,5}=dy;
	conn = pq_connect(setdbopts('dbname','examen1','host','localhost',
	'port','5432','user','postgres','password','lin_$$33'));
	N=pq_exec_params(conn, "insert into ejercicio1(edad, cumpleaños, año, mes, dia) values($1,$2,$3,$4,$5);",params);
	m=(input('Quiere ver historial?(y=1/n=2)'))
	if m == 1
		conn = pq_connect(setdbopts('dbname','examen1','host','localhost',
		'port','5432','user','postgres','password','lin_$$33'));
		N=pq_exec_params(conn, "Select * from ejercicio11;"); 
		disp(N)

	endif
endwhile
