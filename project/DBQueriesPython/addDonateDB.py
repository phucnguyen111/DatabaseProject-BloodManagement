import psycopg2
'''
This function is used to populate the addDonate table when donor register blood donation.
Will be used in add new blood entry
'''

def addDonate(donDonID, bID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodBank")

        cursor = connection.cursor()

        print("Adding donate: ", donDonID,"~",bID)

        sql_insert_query = """insert into Donate values (%s,%s)"""
        record_to_insert = (donDonID,bID)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "records sucessfully added into Donate table")
    except(Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record in to Donate table!", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# donDonID = "123456_160520"
# bID = "123456_160520"
# addDonate(donDonID, bID)