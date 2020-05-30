import psycopg2

'''
This function is used to populate the addDonor table when donor register blood donation.
Will be used in add new blood entry
'''


def addDonor(donDonID, donPerID, donName, donGender, donAddress, donEmail, donCont):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="ha3171999",
                                      host="localhost",
                                      port="5432",
                                      database="BloodBank")
        cursor = connection.cursor()

        print("Adding donor: ",donDonID,"~",donPerID,"~",donName,"~"+donGender,"~",donAddress,"~",donEmail,"~",donCont)

        sql_insert_query = """insert into Donor(DonorID, PersonalID, Name, Gender, Address, Email, ContactNumber) values(%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (donDonID, donPerID, donName, donGender, donAddress, donEmail, donCont)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully inserted into Donor table...")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record to Donor:", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# donDonID = "123456_160520"
# donPerID = 123456
# donName = "Jonah Hex"
# donGender = "Male"
# donAddress = "NewYork"
# donEmail = "Hexxa88@gmail.com"
# donCont = "IJNNIJIWWDE2U04"
#
#
# addDonor(donDonID, donPerID,donName, donGender, donAddress, donEmail, donCont)