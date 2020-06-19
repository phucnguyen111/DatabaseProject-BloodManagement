import psycopg2
from DBQueriesPython.databaseInfo import user, password, host, port, database
'''
This function is used to populate the addDonor table when donor register blood donation.
If addDonor is successful, we continue to addBloodDB
@param[in]:     donPerID        Donor's personal ID
@param[in]:     donName         Donor's name
@param[in]:     donGender       Donor's gender
@param[in]:     donAddress      Donor's address
@param[in]:     donEmail        Donor's email
@param[in]:     donContact      Donor's contact number

@return         status          Table adding status
                1               Success
                0               Failure
'''


def addDonor(donPerID, donName, donGender, donAddress, donEmail, donContact):
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()

        print("Adding donor: ", donPerID, "~", donName, "~", donGender, "~", donAddress, "~", donEmail, "~", donContact)
        sql_insert_query = """insert into Donor(PersonalID, Name, Gender, Address, Email, ContactNumber) values(%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (donPerID, donName, donGender, donAddress, donEmail, donContact)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()

        count = cursor.rowcount
        return 1

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into Donor:", error)
            return 0
    finally:
        if(connection):
            cursor.close()
            connection.close()
