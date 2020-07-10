--Postgres SQL
--QUERY TO DROP ALL TABLES

DO $$ DECLARE
  r RECORD;
BEGIN
  FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
    EXECUTE 'DROP TABLE ' || quote_ident(r.tablename) || ' CASCADE';
  END LOOP;
END $$;
--END

--CREATING TABLES
CREATE TABLE Donor (
	PersonalID BIGINT PRIMARY KEY,
	Name VARCHAR(50),
	Gender VARCHAR(10),
	Address VARCHAR(100),
	Email VARCHAR(30),
	ContactNumber VARCHAR(15)
);

CREATE TABLE BloodGroup(
	BloodType VARCHAR(10) PRIMARY KEY,
	TotalAmount FLOAT NOT NULL
);

CREATE TABLE Hospital (
	HospitalID SERIAL NOT NULL PRIMARY KEY,
	Name VARCHAR(100),
	Address VARCHAR(100),
	Email VARCHAR(30),
	ContactNumber VARCHAR(15)
);

CREATE TABLE Blood (
	BloodID SERIAL NOT NULL PRIMARY KEY,
	PersonalID BIGINT,
	BloodType VARCHAR(10),
	Amount FLOAT,
	DonationDate DATE,
	
	CONSTRAINT BloodForeignKey1 FOREIGN KEY(PersonalID) REFERENCES Donor(PersonalID)
	ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT BloodForeignKey2 FOREIGN KEY(BloodType) REFERENCES BloodGroup(BloodType)
	ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE RequestBloodHistory (
	HospitalID SERIAL NOT NULL,
	BloodType VARCHAR(10) NOT NULL,
	RequestDate DATE,
	RequestAmount FLOAT,
	
	CONSTRAINT RequestPrimaryKey PRIMARY KEY (HospitalID, BloodType, RequestDate),
	CONSTRAINT RequestForeignKey1 FOREIGN KEY(HospitalID) REFERENCES Hospital(HospitalID)
	ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT RequestForeignKey2 FOREIGN KEY (BloodType) REFERENCES BloodGroup(BloodType)
	ON DELETE CASCADE ON UPDATE CASCADE
);
--END

-----------------------------------------------------------------------------------------------------------------------------
--Khoi tao data cho bang BloodGroup
INSERT INTO BloodGroup VALUES ('O+','0'),('O-','0'),('A+','0'),('A-','0'),('B+','0'),('B-','0'),('AB+','0'),('AB-','0');
UPDATE BloodGroup SET TotalAmount = 10 WHERE BloodType = 'O+';
SELECT * FROM Donor;
SELECT * FROM BloodGroup;
SELECT * FROM Blood;
SELECT * FROM Hospital;
SELECT * FROM RequestBloodHistory;
--END

--DELETE ALL DATA FROM TABLES
TRUNCATE TABLE Donate CASCADE;
TRUNCATE TABLE Donor CASCADE;
TRUNCATE TABLE Blood CASCADE;
TRUNCATE TABLE BloodGroup CASCADE;
--END

--TEST
			