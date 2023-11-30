CREATE DATABASE LAB_INDIVIDUAL;


CREATE TABLE orders
(
	ord_num SERIAL PRIMARY KEY,
	ord_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE points
(
	snils char(14) PRIMARY KEY,
	sum_points integer CHECK (sum_points > 0)
);

CREATE TABLE applicants
(
	reg_num SERIAL PRIMARY KEY,
	snils CHAR(14) REFERENCES points
);

CREATE TABLE contests
(
	cont_id SERIAL PRIMARY KEY,
	cont_type text,
	form_of_study text,
	lvl_education text
);

CREATE TABLE positions
(
	position_id SERIAL PRIMARY KEY,
	position_name text
);

CREATE TABLE staff
(
	staff_id SERIAL PRIMARY KEY,
	staff_name TEXT,
	position_id INTEGER REFERENCES positions
);

CREATE TABLE programs
(
	program_id SERIAL PRIMARY KEY,
	program_name TEXT
);

CREATE TABLE accountings
(
	reg_num INTEGER REFERENCES applicants CHECK (reg_num > 0),
	program_id INTEGER REFERENCES programs CHECK (program_id > 0),
	cont_id INTEGER REFERENCES contests CHECK (cont_id > 0) NOT NULL,
	ord_num INTEGER REFERENCES orders CHECK (ord_num > 0) NOT NULL,
	staff_id INTEGER REFERENCES staff CHECK (staff_id > 0) NOT NULL,
	PRIMARY KEY (reg_num,program_id)
);

INSERT INTO orders(ord_date)
VALUES 
('2022-01-13'),
('2023-05-17'),
('1998-12-14');

INSERT INTO points(snils, sum_points)
VALUES 
('ХХХ-ХХХ-ХХХ YY','180'),
('123-456-789 01','189'),
('234-567-890 12','213'),
('345-678-901 23','300');

INSERT INTO applicants(snils)
VALUES 
('ХХХ-ХХХ-ХХХ YY'),
('123-456-789 01'),
('345-678-901 23');

INSERT INTO contests(cont_type, form_of_study, lvl_education)
VALUES 
('бюджет','очная','бакалавриат'),
('внебюджет','заочная','магистратура'),
('бюджет','очно-заочная','аспирантура');

INSERT INTO positions(position_name)
VALUES 
('директор'),
('бухгалтер'),
('стажер');

INSERT INTO staff(staff_name,position_id)
VALUES 
('Александр','1'),
('Анна','2'),
('Алексей','2');

INSERT INTO programs(program_name)
VALUES 
('Информатика'),
('ИСиТ'),
('лучшее'),
('направление');

INSERT INTO accountings(reg_num, program_id, cont_id, ord_num, staff_id)
VALUES 
('1','1','1','1','1'),
('2','1','2','2','3'),
('3','1','1','1','1');