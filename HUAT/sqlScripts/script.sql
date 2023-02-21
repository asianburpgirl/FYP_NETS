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
  	PRIMARY KEY (carparkID));

INSERT INTO carparkDetails(carparkName,carparkLocation,latitude, longitude ,imagePath,maxCapacity,currentCapacity, hourlyweekdaypeak,hourlyweekdaynonpeak,hourlyweekendpeak,hourlyweekendnonpeak,seasonweekdaypeak,seasonweekdaynonpeak,seasonweekendpeak,seasonweekendnonpeak) VALUES 
("ION Orchard","2 Orchard Turn, Singapore 238801",1.3062193796555794, 103.83284067837033, "assets/images/ion.jpg",82, 82,2.5,2,3,2.5,16,12,135,143),
("313@Somerset","313 Orchard Rd, Singapore 238895",1.3027040784855177, 103.83847162015051,"assets/images/313.jpg", 100, 40,3,1.5,10,5,124,187,135,176),
("Paragon Shopping Centre","290 Orchard Rd, Singapore 238859",1.304487326883736, 103.83602458835058,"assets/images/paragon.jpg", 85, 41,4,4,8,4.5,124,187,135,176),
("*SCAPE","2 Orchard Link, Singapore 237978",1.3021316002091397, 103.83596093628584,"assets/images/scape.jpg", 85, 20,4.5,4,7.5,7.5,124,187,135,176),
("Takashimaya Shopping Centre","391 Orchard Rd, Singapore 238872",1.303263206539862, 103.83459342778606,"assets/images/takashimaya.jpeg", 70, 0,5,3,6,3,124,187,135,176),
("Tangs Plaza","310 Orchard Road Tang Plaza, 238864",1.3056964883694633, 103.83310108195877,"assets/images/tangs.jpg", 105, 90,4,3.5,10,9,124,187,135,176),
("Wheelock Place","501 Orchard Rd, Singapore 238880",1.3055296648422483, 103.83049454423592, "assets/images/Wheelock.png",30, 30,5,4.5,7,5,.5198,112,135,134),
("Wisma Atria","435 Orchard Rd, Singapore 238877",1.304149158199214, 103.83327760043642, "assets/images/wisma.jpeg",103, 29,6.50,3,8.5,7,123,143,135,198);


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
