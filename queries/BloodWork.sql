CREATE TABLE Donor (
	DonorID SERIAL NOT NULL PRIMARY KEY,
	Name VARCHAR(50),
	Gender VARCHAR(10),
	--DateOfBirth DATE,
	Address VARCHAR(100),
	Email VARCHAR(30),
	ContactNumber VARCHAR(15),
	BloodGroup VARCHAR(5),
	MedicalReport VARCHAR(200)
);

CREATE TABLE Blood (
	BloodID SERIAL NOT NULL PRIMARY KEY,
	Amount INT,
	Status VARCHAR(20)
);

CREATE TABLE Hospital (
	HospitalID SERIAL NOT NULL PRIMARY KEY,
	Name VARCHAR(100),
	Address VARCHAR(100),
	ContactNumber VARCHAR(15), 
	Email VARCHAR(30)
);

CREATE TABLE BloodProduct(
ProductID SERIAL NOT NULL PRIMARY KEY,
Name VARCHAR(50),
Type VARCHAR(10),
Amount INT
);

CREATE TABLE Donate (
	DonorID INT NOT NULL,
	BloodID INT NOT NULL,
	DonationDate DATE,
	CONSTRAINT PrimaryKeyDonate PRIMARY KEY (DonorID, BloodID),
	CONSTRAINT ForeignKeyDonate1 FOREIGN KEY (DonorID) REFERENCES Donor(DonorID),
	CONSTRAINT ForeignKeyDonate2 FOREIGN KEY(BloodID) REFERENCES Blood(BloodID)
);

CREATE TABLE BelongsTo (
	BloodID INT NOT NULL,
	ProductID INT NOT NULL,

	CONSTRAINT PrimaryKeyBelongsTo PRIMARY KEY (ProductID, BloodID),
	CONSTRAINT ForeignKeyBelongsTo1 FOREIGN KEY (ProductID) REFERENCES BloodProduct(ProductID),
	CONSTRAINT ForeignKeyBelongsTo2 FOREIGN KEY(BloodID) REFERENCES Blood(BloodID)
);

CREATE TABLE DistributeBlood (
	ProductID INT NOT NULL,
	HospitalID INT NOT NULL,
	DistributionDate DATE,

	CONSTRAINT PrimaryKeyDistributeBlood PRIMARY KEY (ProductID, HospitalID),
	CONSTRAINT ForeignKeyDistributeBlood1 FOREIGN KEY (ProductID) REFERENCES BloodProduct(ProductID),
	CONSTRAINT ForeignKeyDistributeBlood2 FOREIGN KEY (HospitalID) REFERENCES Hospital(HospitalID)
);