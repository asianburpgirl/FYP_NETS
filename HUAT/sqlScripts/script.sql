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
    bookingAmt FLOAT NOT NULL, 
    userID INT NOT NULL , 
    PRIMARY KEY (bookingID));
	
INSERT INTO `bookings` (`bookingID`, `bookingDateTime`, `bookingLocation`, `locationName`,`bookingStartDateTime`, `bookingEndDateTime`, `status`, `bookingRef`, `bookingAmt`, `userID`) 
VALUES (NULL, CURRENT_TIMESTAMP,  'Funan','99 City Hall Street, Singapore 755666', '2023-02-01 15:30:00', '2023-02-01 11:30:00', 'Booked', 'aasS234Fa3Af3ff319fD', 1.50, '1');
INSERT INTO `bookings` (`bookingID`, `bookingDateTime`, `bookingLocation`, `locationName`,`bookingStartDateTime`, `bookingEndDateTime`, `status`, `bookingRef`, `bookingAmt`, `userID`) 
VALUES (NULL, '2023-01-27 12:33:10', 'ION Orchard', '123 Orchard Street, Singapore 712345', '2023-01-30 12:30:00', '2023-01-30 12:30:00', 'Booked', 'S124fdf13Rafdf', 3.01, '2');
INSERT INTO `bookings` (`bookingID`, `bookingDateTime`, `bookingLocation`, `locationName`, `bookingStartDateTime`, `bookingEndDateTime`, `status`, `bookingRef`, `bookingAmt`, `userID`) 
VALUES (NULL, '2023-01-27 12:43:10', 'ION Orchard', '123 Orchard Street, Singapore 712345', '2023-01-28 12:00:00', '2023-01-28 01:00:00', 'Booked', '22afsadsf4df13Rafdf', 2.51, '1');
INSERT INTO `bookings` (`bookingID`, `bookingDateTime`, `bookingLocation`, `locationName`, `bookingStartDateTime`, `bookingEndDateTime`, `status`, `bookingRef`, `bookingAmt`, `userID`) 
VALUES (NULL, '2023-01-27 12:43:10', 'ION Orchard', '123 Orchard Street, Singapore 712345', '2023-01-28 12:00:00', '2023-01-28 01:00:00', 'Booked', '22afsadsf4df13Rafdf', 12.10, '2');
INSERT INTO `bookings` (`bookingID`, `bookingDateTime`, `bookingLocation`, `locationName`, `bookingStartDateTime`, `bookingEndDateTime`, `status`, `bookingRef`, `bookingAmt`, `userID`) 
VALUES (NULL, '2023-01-27 12:43:10', 'ION Orchard', '123 Orchard Street, Singapore 712345', '2023-01-28 12:00:00', '2023-01-28 01:00:00', 'Booked', '22afsadsf4df13Rafdf', 0.51, '2');

CREATE TABLE subscriptions( 
	subscriptionID INT(11) NOT NULL AUTO_INCREMENT , 
    subscriptionType VARCHAR(128) NOT NULL ,
    subscriptionsStartTime DATETIME NOT NULL, 
    subscriptionsEndTime DATETIME NOT NULL, 
    bookingLocation VARCHAR(128) NOT NULL , 
    locationName VARCHAR(128) NOT NULL ,
    status VARCHAR(128) NOT NULL , 
    subscriptionRef VARCHAR(128) NOT NULL,
    subscriptionAmt FLOAT(5,2) NOT NULL, 
    userID INT NOT NULL , 
    PRIMARY KEY (subscriptionID));
	
INSERT INTO `subscriptions` (`subscriptionID`, `subscriptionType`, `subscriptionsStartTime`, 
`subscriptionsEndTime`, `bookingLocation`, `locationName`, 
`status`,  `subscriptionRef`, `subscriptionAmt`, `userID`) 
VALUES (NULL, 'Hourly','2023-02-01 15:30:00', '2023-02-05 15:30:00',
'Funan','99 City Hall Street, Singapore 755666', 'Subscribed', 'aasS234Fa3Af3ff319fD', 1.00, '1');

INSERT INTO `subscriptions` (`subscriptionID`, `subscriptionType`,`subscriptionsStartTime`, 
`subscriptionsEndTime`, `bookingLocation`, `locationName`, 
 `status`,  `subscriptionRef`, `subscriptionAmt`, `userID`) 
VALUES (NULL, 'Complmentary','2023-02-01 12:30:00', '2023-02-05 15:30:00',
'Funan','99 City Hall Street, Singapore 755666', 'Subscribed', 'b1sS2a4FA5Af3f5d19fT', 100.51, '1');

INSERT INTO `subscriptions` (`subscriptionID`, `subscriptionType`,`subscriptionsStartTime`, 
`subscriptionsEndTime`, `bookingLocation`, `locationName`, 
 `status`,  `subscriptionRef`, `subscriptionAmt`, `userID`) 
VALUES (NULL, 'Complmentary','2023-02-01 12:30:00', '2023-02-15 17:00:00',
'Funan','99 City Hall Street, Singapore 755666', 'Subscribed', '1SsS26A4A5Af3Ufd19Y3', 0, '2');


CREATE TABLE carparkDetails (
	carparkID INT NOT NULL AUTO_INCREMENT,
    carparkName VARCHAR(128) NOT NULL,
	carparkLocation VARCHAR(128) NOT NULL,
	maxCapacity INT NOT NULL , 
	currentCapacity INT NOT NULL  DEFAULT '0', 
	hourlyweekdaypeak INT NOT NULL,
    hourlyweekdaynonpeak INT NOT NULL,
    hourlyweekendpeak INT NOT NULL,
    hourlyweekendnonpeak INT NOT NULL,
    seasonweekdaypeak INT NOT NULL,
    seasonweekdaynonpeak INT NOT NULL,
    seasonweekendpeak INT NOT NULL,
    seasonweekendnonpeak INT NOT NULL,
  	PRIMARY KEY (carparkID));

INSERT INTO carparkDetails(carparkName,carparkLocation,maxCapacity,currentCapacity, hourlyweekdaypeak,hourlyweekdaynonpeak,hourlyweekendpeak,hourlyweekendnonpeak,seasonweekdaypeak,seasonweekdaynonpeak,seasonweekendpeak,seasonweekendnonpeak) VALUES 
("ION Orchard","123 Orchard Road",82, 20,200,150,300,250,165,124,135,143),
("Funan","1 City Hall Road",85, 4,234,112,323,225,124,187,135,176),
("Sunplaza","99 Sembawang Drive",30, 1,245,123,354,252,198,112,135,134),
("Plaza Sing","12 Dhobby Gaut Avenue",103, 29,212,143,366,225,123,143,135,198);

CREATE TABLE users (
	userID INT(11) NOT NULL AUTO_INCREMENT,
	email VARCHAR(128) NOT NULL,
	name VARCHAR(128) NOT NULL,
	phoneNum INT NOT NULL,
	username VARCHAR(128) NOT NULL,
	password VARCHAR(128) NOT NULL,
	balance FLOAT(5,2),
  	PRIMARY KEY (userID));

INSERT INTO users(email, name, phoneNum, username, password, balance) VALUES
("johntan99@gmail.com","John Tan", 91234567, "johntan99", "admin123", 1.23);
INSERT INTO users(email, name, phoneNum, username, password, balance) VALUES
("testLimIsSmart@gmail.com","Test Lim", 92345678, "test", "test", 92.42);
INSERT INTO users(email, name, phoneNum, username, password, balance) VALUES
("testtest@gmail.com","Test Tan", 91234567, "test2", "test2", 9.10);
