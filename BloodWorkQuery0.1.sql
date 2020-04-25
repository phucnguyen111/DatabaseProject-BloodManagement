CREATE TABLE Donor (
	DonorID SERIAL NOT NULL PRIMARY KEY,
	Name VARCHAR(50),
	DateOfBirth DATE,
	Address VARCHAR(100),
	--Gender VARCHAR(10),
	ContactNumber VARCHAR(15),
	BloodGroup VARCHAR(5),
	Email VARCHAR(30),
	MedicalReport VARCHAR(200)
);

CREATE TABLE Blood (
	BloodID SERIAL NOT NULL PRIMARY KEY, --> Why need BloodID when there's already DonorID? Import constraint Donor(DonorID) instead?
	Amount INT,
	Status VARCHAR(20)
	--TestResult VARCHAR(5) --> Why removed? Necessary?( A+, B-, O+, AB, ...)
);

CREATE TABLE Hospital (
	HospitalID SERIAL NOT NULL PRIMARY KEY,
	Name VARCHAR(100),
	Address VARCHAR(100),
	ContactNumber VARCHAR(15), 
	Email VARCHAR(30)
);

CREATE TABLE BloodBank (
	BankID SERIAL NOT NULL PRIMARY KEY,
	Name VARCHAR(100),
	Address VARCHAR(100),
	ContactNumber VARCHAR(15), 
	Email VARCHAR(30)
);

CREATE TABLE Donor_Donate_Blood (
	DonorID INT NOT NULL,
	BloodID INT NOT NULL,
	DonationDate DATE,
	CONSTRAINT PrimaryKeyDonate PRIMARY KEY (DonorID, BloodID),
	CONSTRAINT ForeignKeyDonate1 FOREIGN KEY (DonorID) REFERENCES Donor(DonorID),
	CONSTRAINT ForeignKeyDonate2 FOREIGN KEY(BloodID) REFERENCES Blood(BloodID)
);

CREATE TABLE Blood_BelongsTo_BloodBank (
	BloodID INT NOT NULL,
	BankID INT NOT NULL,

	CONSTRAINT PrimaryKeyBelongsTo PRIMARY KEY (BankID, BloodID),
	CONSTRAINT ForeignKeyBelongsTo1 FOREIGN KEY (BankID) REFERENCES BloodBank(BankID),
	CONSTRAINT ForeignKeyBelongsTo2 FOREIGN KEY(BloodID) REFERENCES Blood(BloodID)
);

CREATE TABLE BloodBank_ManageInfo_Donor (
	DonorID INT NOT NULL,
	BankID INT NOT NULL,

	CONSTRAINT PrimaryKeyManageInfo PRIMARY KEY (DonorID, BankID),
	CONSTRAINT ForeignKeyManageInfo1 FOREIGN KEY (DonorID) REFERENCES Donor(DonorID),
	CONSTRAINT ForeignKeyManageInfo2 FOREIGN KEY (BankID) REFERENCES BloodBank(BankID)
);

CREATE TABLE BloodBank_DistributeBlood_Hospital (
	BankID INT NOT NULL,
	HospitalID INT NOT NULL,
	DistributionDate DATE,

	CONSTRAINT PrimaryKeyDistributeBlood PRIMARY KEY (BankID, HospitalID),
	CONSTRAINT ForeignKeyDistributeBlood1 FOREIGN KEY (BankID) REFERENCES BloodBank(BankID),
	CONSTRAINT ForeignKeyDistributeBlood2 FOREIGN KEY (HospitalID) REFERENCES Hospital(HospitalID)
);