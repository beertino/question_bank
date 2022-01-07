CREATE TABLE "Car" (
	"VIN"	TEXT,
	"Brand"	TEXT,
	"VehicleType"	TEXT,
	"EnergySource"	TEXT,
	"DailyPrice"	REAL,
	"Availability"	TEXT,
	PRIMARY KEY("VIN")
);

CREATE TABLE "Customer" (
	"CustomerID"	INTEGER,
	"Name"	TEXT,
	"Gender"	TEXT,
	"Contact"	TEXT,
	PRIMARY KEY("CustomerID" AUTOINCREMENT)
);

CREATE TABLE "RentalPoint" (
	"PointID"	INTEGER,
	"Address"	TEXT,
	"OpWeekDay"	TEXT,
	"OpStartHr"	TEXT,
	"OpEndHr"	TEXT,
	PRIMARY KEY("PointID" AUTOINCREMENT)
);

CREATE TABLE "RentalRecord" (
	"CustomerID"	INTEGER,
	"VIN"	INTEGER,
	"StartDate"	TEXT,
	"CollectionPointID"	INTEGER,
	"ReturnDate"	TEXT,
	"ReturnPointID"	INTEGER,
	PRIMARY KEY("CustomerID","VIN","StartDate"),
	FOREIGN KEY("CollectionPointID") REFERENCES "RentalPoint"("PointID"),
	FOREIGN KEY("CustomerID") REFERENCES "Customer"("CustomerID"),
	FOREIGN KEY("VIN") REFERENCES "Car"("VIN")
)