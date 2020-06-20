import psycopg2
from DBQueriesPython.databaseInfo import user, password, host, port, database
'''
This function is used to populate the addblood table when donor register blood donation.
Will be used in add new blood entry
'''

def addBlood(bID, bAmount, bStatus):
    try:
        connection = psycopg2.connect(user = user,
                                      password = password,
                                      host = host,
                                      port = port,
                                      database = database)
        cursor = connection.cursor()

        print("Adding blood: ",bID,"~",bAmount,"~"+bStatus)

        sql_insert_query = """insert into Blood values(%s,%s,%s,NOW())"""
        record_to_insert = (bID, bAmount, bStatus)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully inserted into Blood table...")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record to Blood:", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# bID = "123456_160520"
# bAmount = 100
# bStatus = "Good"
# addBlood(bID,bAmount,bStatus)