# Task 4

CREATE TABLE "Book" (
	"BookID"	INTEGER,
	"Title"	TEXT,
	"Price"	NUMERIC,
	"Type"	TEXT,
	PRIMARY KEY("BookID")
);

CREATE TABLE "Printed" (
	"BookID"	INTEGER,
	"Title"	TEXT,
	"Price"	NUMERIC,
	"Type"	TEXT,
	"Weight" NUMERIC,
	PRIMARY KEY("BookID")
);

CREATE TABLE "Virtual" (
	"BookID"	INTEGER,
	"Title"	TEXT,
	"Price"	NUMERIC,
	"Type"	TEXT,
	"DownloadLink"	TEXT,
	PRIMARY KEY("BookID")
);