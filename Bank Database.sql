CREATE DATABASE bank;

USE bank;

CREATE TABLE account
  (
    fname VARCHAR(30),
    acno VARCHAR(10),
    dob DATE,
    ad VARCHAR(50),
    phn VARCHAR(10),
    ob INT,
    CONSTRAINT acno_pk PRIMARY KEY(acno)
  );
  
CREATE TABLE amount
  (
	 fname VARCHAR(30),
     acno VARCHAR(10),
     balance INT
  );
  
DESCRIBE account;

DESCRIBE amount;