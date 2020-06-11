import psycopg2
'''
This function is used to populate the addblood table when donor register blood donation.
Will be used in add new blood entry
'''

def addBlood(bAmount, bStatus):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()

        print("Adding blood: ",bAmount,"~"+bStatus)

        sql_insert_query = """insert into Blood(Amount, DonationDate) values(%s,NOW())"""
        record_to_insert = (bAmount, bStatus)
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