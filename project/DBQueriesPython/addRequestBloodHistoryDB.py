import psycopg2

def addRequestBloodHistory(rbhHospitalID, rbhBloodType, rbhRequestDate, rbhRequestAmount):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()

        print("Adding blood request history: ", rbhHospitalID, "~", rbhBloodType, "~" + rbhRequestDate, "~", rbhRequestAmount)
        sql_insert_query = """insert into  RequestBloodHistory(HospitalID, BloodType, RequestDate, RequestAmount) values(%s,%s,%s,%s)"""
        record_to_insert = (rbhHospitalID, rbhBloodType, rbhRequestDate, rbhRequestAmount)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()

        count = cursor.rowcount
        print(count, "records successfully inserted into Donor table...")

    except(Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into RequestBloodHistory table: ", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# rbhHospitalID = 1
# rbhBloodType = "A-"
# rbhRequestDate = "2020-04-02"
# rbhRequestAmount = 132
# addRequestBloodHistory(rbhHospitalID, rbhBloodType, rbhRequestDate, rbhRequestAmount)