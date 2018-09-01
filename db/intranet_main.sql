create database intranet;
use intranet;
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
create table clients(
	id int not null auto_increment primary key,
	name varchar(50) not null,
	address varchar(300),
	phone varchar(100),
	mobile varchar(10) not null,
	password_string varchar(50) not null,
	password varchar(50) not null,
	zone int not null,
    plan int not null,
	region tinyint,
	type enum('personal','company') default 'personal',
	pan varchar(10),
	email varchar(50),
	send_sms enum('yes','no') default 'yes',
	comments text,
    foreign key(zone) references zones(id),
    foreign key(plan) references plans(id)
) engine=innoDb;

alter table clients change send_sms send_sms enum('yes','no') default 'yes';
