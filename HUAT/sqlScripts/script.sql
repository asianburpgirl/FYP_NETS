DROP SCHEMA IF EXISTS localconnect;
CREATE SCHEMA localconnect;
USE localconnect;

CREATE TABLE bookings( 
	bookingID INT(11) NOT NULL AUTO_INCREMENT , 
    bookingDateTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP , 
    bookingLocation VARCHAR(128) NOT NULL , 
    locationName VARCHAR(128) NOT NULL, 
    bookingStartDateTime DATETIME NOT NULL , 
    bookingEndDateTime DATETIME NOT NULL , 
    status VARCHAR(128) NOT NULL , 
    bookingRef VARCHAR(128) NOT NULL,
    bookingAmt FLOAT(5,2) NOT NULL, 
    userID INT NOT NULL , 
    PRIMARY KEY (bookingID));
	
INSERT INTO `bookings` (`bookingID`, `bookingDateTime`, `bookingLocation`, `locationName`,`bookingStartDateTime`, `bookingEndDateTime`, `status`, `bookingRef`, `bookingAmt`, `userID`) 
VALUES (NULL, CURRENT_TIMESTAMP,  'ION Orchard','2 Orchard Turn, Singapore 238801', '2023-02-01 15:30:00', '2023-02-01 11:30:00', 'Booked', 'aasS234Fa3Af3ff319fD', 1.50, '3'),
(NULL, '2023-01-28 11:30:00', 'ION Orchard', '2 Orchard Turn, Singapore 238801', '2023-01-30 12:30:00', '2023-01-30 12:30:00', 'Booked', 'S124fdf13Rafdf', 3.01, '3'),
(NULL, '2023-01-30 16:03:12', 'Paragon Shopping Centre','290 Orchard Rd, Singapore 238859', '2023-01-28 12:00:00', '2023-01-28 01:00:00', 'Booked', '22afsadsf4df13Rafdf', 2.51, '3'),
(NULL, '2023-02-01 12:43:50', '*SCAPE', '2 Orchard Link, Singapore 237978', '2023-01-28 12:00:00', '2023-01-28 01:00:00', 'Booked', '22afsadsf4df13Rafdf', 12.10, '3'),
(NULL, '2023-05-05 12:44:10', 'Wisma Atria', '435 Orchard Rd, Singapore 238877', '2023-01-28 12:00:00', '2023-01-28 01:00:00', 'Booked', '22afsadsf4df13Rafdf', 0.51, '3');

CREATE TABLE subscriptions( 
	subsID INT(11) NOT NULL AUTO_INCREMENT , 
    -- subsDateTime DATETIME NOT NULL, 
    subsDateTime INT NOT NULL,  
    subsTypeID VARCHAR(128) NOT NULL ,
    status VARCHAR(128) NOT NULL , 
    subsRef VARCHAR(128) NOT NULL,
    subsAmt FLOAT(5,2) NOT NULL, 
    userID INT NOT NULL , 
    PRIMARY KEY (subsID));


CREATE TABLE carparkDetails (
	carparkID INT NOT NULL AUTO_INCREMENT,
    carparkName VARCHAR(128) NOT NULL,
	carparkLocation VARCHAR(128) NOT NULL,
    latitude FLOAT(15,10) NOT NULL,
    longitude FLOAT(15,10) NOT NULL,
    imagePath VARCHAR(128) NOT NULL,
	maxCapacity INT NOT NULL , 
	currentCapacity INT NOT NULL  DEFAULT '0', 
	hourlyweekdaypeak FLOAT(4,2) NOT NULL,
    hourlyweekdaynonpeak FLOAT(4,2) NOT NULL,
    hourlyweekendpeak FLOAT(4,2) NOT NULL,
    hourlyweekendnonpeak FLOAT(4,2) NOT NULL,
    seasonweekdaypeak INT NOT NULL,
    seasonweekdaynonpeak INT NOT NULL,
    seasonweekendpeak INT NOT NULL,
    seasonweekendnonpeak INT NOT NULL,
    chosen INT NOT NULL,
  	PRIMARY KEY (carparkID));

INSERT INTO carparkDetails(carparkName,carparkLocation,latitude, longitude ,imagePath,maxCapacity,currentCapacity, hourlyweekdaypeak,hourlyweekdaynonpeak,hourlyweekendpeak,hourlyweekendnonpeak,seasonweekdaypeak,seasonweekdaynonpeak,seasonweekendpeak,seasonweekendnonpeak,chosen) VALUES 
("ION Orchard","2 Orchard Turn, Singapore 238801",1.3041540462448922, 103.83195992607827, "assets/images/ion.jpg",82, 82,2.5,2,3,2.5,16,12,135,143,1),
("Paragon Shopping Centre","290 Orchard Rd, Singapore 238859",1.3040258775031617, 103.83608284915861,"assets/images/paragon.jpg", 85, 41,4,4,8,4.5,124,187,135,176,1),
("Takashimaya Shopping Centre","391 Orchard Rd, Singapore 238872",1.3033454254185042, 103.83455711763565,"assets/images/takashimaya.jpeg", 70, 0,5,3,6,3,124,187,135,176,0),
("Tangs Plaza","310 Orchard Road Tang Plaza, 238864",1.3050314731714412, 103.83297614415605,"assets/images/tangs.jpg", 105, 90,4,3.5,10,9,124,187,135,176,1),
("Wheelock Place","501 Orchard Rd, Singapore 238880",1.3048859701842488, 103.83048138946437, "assets/images/Wheelock.png",30, 30,5,4.5,7,5,.5198,112,135,134,1),
("313@Somerset","313 Orchard Rd, Singapore 238895",1.301171207812743, 103.8386220085623,"assets/images/313.jpg", 100, 40,3,1.5,10,5,124,187,135,176,0),
("*SCAPE","2 Orchard Link, Singapore 237978",1.3010677408660067, 103.83576204980196,"assets/images/scape.jpg", 85, 20,4.5,4,7.5,7.5,124,187,135,176,0),
("Wisma Atria","435 Orchard Rd, Singapore 238877",1.303842974291844, 103.8333226716273, "assets/images/wisma.jpeg",103, 29,6.50,3,8.5,7,123,143,135,198,0);


CREATE TABLE users (
	userID INT(11) NOT NULL AUTO_INCREMENT,
	email VARCHAR(128) NOT NULL,
	name VARCHAR(128) NOT NULL,
	phoneNum INT NOT NULL,
	username VARCHAR(128) NOT NULL,
	password VARCHAR(128) NOT NULL,
	balance FLOAT(5,2) NOT NULL DEFAULT '0',
    role VARCHAR(128) NOT NULL,
  	PRIMARY KEY (userID));

INSERT INTO users(email, name, phoneNum, username, password, balance,role) VALUES
("johntan99@gmail.com","John Tan", 91234567, "johntan99", "admin123", 1.23 , "Admin"),
("testLimIsSmart@gmail.com","Test Lim", 92345678, "test", "test", 92.42, "Admin"),
("testtest@gmail.com","Test Tan", 91234567, "test2", "test2", 43.10, "User");



CREATE TABLE transaction (
    transID INT(11) NOT NULL AUTO_INCREMENT,
    transDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP , 
    transType VARCHAR(128) NOT NULL , 
    amount FLOAT(5,2) NOT NULL, 
    userID INT NOT NULL , 
    PRIMARY KEY (transID));

INSERT INTO `transaction` (`transID`, `transDate`, `transType`, `amount`,`userID`) VALUES
(NULL, '2023-01-06 22:58:38', 'topup', 11.00, '3'),
(NULL, '2023-03-06 23:58:38', 'deduct', 1.02, '3'),
(NULL, '2023-03-16 13:58:38', 'topup', 5.00, '3');


