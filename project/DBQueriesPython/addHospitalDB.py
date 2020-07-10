import psycopg2
from DBQueriesPython.databaseInfo import user, password, host, port, database
'''
This function is used to populate the Hospital table when donor register blood donation.
@param[in]:     hName        Hospital's name
@param[in]:     hAddress     Hospital's address
@param[in]:     hEmail       Hospital's email
@param[in]:     hContact     Hospital's contact number

@return         status          Table adding status
                1               Success
                0               Failure
'''


def addHospital(hName, hAddress, hEmail, hContact): 
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()

        print("Adding hospital:")
        print("+ Name: " + hName)
        print("+ Address: " + hAddress)
        print("+ Email: " + hEmail)
        print("+ Contact: " + hContact)

        sql_insert_query = """insert into Hospital(Name, Address, Email, ContactNumber) values(%s,%s,%s,%s)"""
        record_to_insert = (hName, hAddress, hEmail, hContact)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()

        count = cursor.rowcount
        print(count, "records successfully inserted into Hospital table...")
        return 1
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into Hospital table:", error)
            return 0
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#---------------------------------------------------------------
#Return values:
#1: Added into table
#0: Database error -> not added