create database mydb;

CREATE TABLE if not exists work_log (
id int(100) NOT NULL AUTO_INCREMENT,
work_perfrom_date date NOT NULL,
hours_worked float(20) NOT NULL,
employee_id int(10) NOT NULL,
job_group VARCHAR(5) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE if not exists report_ids_processed (
id int(100) NOT NULL AUTO_INCREMENT,
report_id int(100) NOT NULL,
PRIMARY KEY (id),
UNIQUE (report_id)
);