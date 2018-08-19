create database intranet;
use intranet;
create table clients(
	id int not null auto_increment primary key,
	name varchar(50) not null,
	address varchar(300),
	phone varchar(100),
	mobile varchar(10) not null,
	password_string varchar(50) not null,
	password varchar(50) not null,
	zone tinyint,
	region tinyint,
	type enum("personal","company") default "personal",
	pan varchar(10),
	email varchar(50),
	send_sms boolean default true,
	comments text
) engine=innoDb;
create table zones(
	id int not null auto_increment primary key,
	name varchar(50) not null
) engine=innoDb;
create table routers(
	id int not null auto_increment primary key,
    name varchar(50) not null
)engine=innoDb;
create table plans(
	id int not null auto_increment primary key,
    name varchar(50) not null,
    price int not null,
    discount int default 0
) engine=innoDb;
show tables;
truncate zones;
desc clients;