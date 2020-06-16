import psycopg2

'''
This function is used to record the hospitals' request for blood. Each time a hospital maké a request, the system will save that request's detail into this table
@param[in]:     rbhHospitalID           Hospital ID of the hospital that is requesting blood history
@param[in]:     rbhBloodType            Blood type that the above hospital wants
@param[in]:     rbhRequestDate          The date the request is made
@param[in]:     rbhRequestAmount        The amount that the above hospital wants

@return         status                  Whether the request history is successful or not
                1                       Request history is successfully added to the table
                0                       Database has error, can not add this record
'''
def addBloodRequestHistory(rbhHospitalID, rbhBloodType, rbhRequestDate, rbhRequestAmount):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="ha3171999",
                                      host="localhost",
                                      port="5432",
                                      database="BloodBank")
        cursor = connection.cursor()

        print("Adding blood request history: ", rbhHospitalID, "~", rbhBloodType, "~" + rbhRequestDate, "~", rbhRequestAmount)
        sql_insert_query = """insert into  RequestBloodHistory(HospitalID, BloodType, RequestDate, RequestAmount) values(%s,%s,%s,%s)"""
        record_to_insert = (rbhHospitalID, rbhBloodType, rbhRequestDate, rbhRequestAmount)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()

        count = cursor.rowcount
        print(count, "records successfully inserted into Donor table...")
        return 1
    except(Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into RequestBloodHistory table: ", error)
            return 0
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
