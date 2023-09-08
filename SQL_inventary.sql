create database if not exists inventary; #create database
use inventary;

truncate inventary; # delete information of table
drop table inventary; # delete table

create table if not exists inventary(
code varchar(10),
product varchar(100),
provider varchar(75),
kind varchar(100),
price decimal (5.3),
quantity int(100),
description text,
primary key(code) );	

insert into inventary values ("BOOKS","book","santillana","Book","1500.00","50","update math book of santillana");
select * from inventary;

#EL PROGRAMA PRINCIPAL DEBE TENER UN ALTER TABLE, QUE PERMITA VER EL VALOR TOTAL DE TODOS LOS PRODUCTOS QUE SE TIENEN.