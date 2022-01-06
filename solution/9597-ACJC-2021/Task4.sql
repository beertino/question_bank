CREATE TABLE "BentoBox" (
	"BentoName"	TEXT,
	"ProductionCost"	NUMERIC,
	"ContainEgg"	INTEGER,
	"ContainNut"	INTEGER,
	"ContainSeafood"	INTEGER,
	PRIMARY KEY("BentoName")
);

CREATE TABLE "Kiosk" (
	"KioskID"	INTEGER,
	"Location"	TEXT,
	"Rating"	NUMERIC,
	PRIMARY KEY("KioskID")
);

CREATE TABLE "KioskBento" (
	"KioskID"	INTEGER,
	"BentoName"	TEXT,
	"SellPrice"	NUMERIC,
	PRIMARY KEY("KioskID")
);