import psycopg2

'''
This function is used to populate the addDonor table when donor register blood donation.
'''


def addDonor(donPerID, donName, donGender, donAddress, donEmail, donCont):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()

        print("Adding donor: ",donPerID,"~",donName,"~"+donGender,"~",donAddress,"~",donEmail,"~",donCont)
        sql_insert_query = """insert into Donor(PersonalID, Name, Gender, Address, Email, ContactNumber) values(%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (donPerID, donName, donGender, donAddress, donEmail, donCont)
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


# donPerID = 123456
# donName = "Jonah Hex"
# donGender = "Male"
# donAddress = "NewYork"
# donEmail = "Hexxa88@gmail.com"
# donCont = "IJNNIJIWWDE2U04"
#
#
# addDonor(donPerID, donName, donGender, donAddress, donEmail, donCont)