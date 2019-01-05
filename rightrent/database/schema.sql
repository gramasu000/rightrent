/* SQL Database Initialization */

/* Drop all tables if they exist and rebuild them*/
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS buildings;
DROP TABLE IF EXISTS apartments;
DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS payments;

/* Create table for user information */
CREATE TABLE users (
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    passwordhash TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    joindate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

/* Create table for building information */
CREATE TABLE buildings (
    buildingid INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (userid) REFERENCES users (userid),
    buildingname TEXT NOT NULL,
    buildingaddress TEXT NOT NULL,
    numberapartments INTEGER NOT NULL DEFAULT 0,
    numberrenters INTEGER NOT NULL DEFAULT 0,
    extrainfo TEXT 
);

/* Create table for apartment information - 'child' of building */
CREATE TABLE apartments (
    apartmentid INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (buildingid) REFERENCES buildings(buildingid),
    FOREIGN KEY (userid) REFERENCES users(userid),
    apartmentnumber TEXT NOT NULL,
    rented BOOLEAN NOT NULL DEFAULT FALSE,
    store BOOLEAN NOT NULL DEFAULT FALSE,
    extrainfo TEXT
);

/* Create table for renter information - 'child' of apartment */
CREATE TABLE renters (
    renterid INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (apartmentid) REFERENCES apartments(apartmentid),
    FOREIGN KEY (buildingid) REFERENCES buildings(buildingid),
    FOREIGN KEY (userid) REFERENCES users(userid),
    name TEXT NOT NULL,
    phonenumber TEXT,
    phonenumber2 TEXT,
    leasestart DATE NOT NULL,
    leaseend DATE NOT NULL,
    leaseterm TEXT NOT NULL,
    leaseended BOOLEAN NOT NULL DEFAULT FALSE,
    balance INTEGER NOT NULL DEFAULT 0,
    extrainfo TEXT 
);

/* Create table for expense information - 'child' of expenses */
CREATE TABLE expenses (
    expenseid INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (renterid) REFERENCES renters(renterid),
    FOREIGN KEY (userid) REFERENCES users(userid),
    name TEXT NOT NULL,
    amount INTEGER NOT NULL,
    issuedate DATE NOT NULL,
    amountpaid INTEGER NOT NULL DEFAULT 0,
    paidornot INTEGER NOT NULL DEFAULT FALSE,
    extrainfo TEXT 
);

/* Create table for renter information - 'child' of payments */
CREATE TABLE payments (
    paymentid INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (expenseid) REFERENCES expenses(expenseid),
    FOREIGN KEY (renterid) REFERENCES renters(renterid),
    FOREIGN KEY (userid) REFERENCES users(userid),
    name TEXT NOT NULL,
    amount INTEGER NOT NULL,
    paymentmethod TEXT NOT NULL,
    paymentdate DATE, NOT NULL,
    extrainfo TEXT
);
