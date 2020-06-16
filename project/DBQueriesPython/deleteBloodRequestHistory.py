import psycopg2

'''
This function is used to delete the hospitals' request for blood's history.
@param[in]:     rbhHospitalID           Hospital ID of the hospital that is requesting blood history
@param[in]:     rbhBloodType            Blood type that the above hospital wants
@param[in]:     rbhRequestDate          The date the request is made


@return         status                  Whether the request history's deletion is successful or not
                1                       Success
                0                       Failure
'''
def deleteBloodRequestHistory(rbhHospitalID, rbhBloodType, rbhRequestDate):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="ha3171999",
                                      host="localhost",
                                      port="5432",
                                      database="BloodBank")
        cursor = connection.cursor()


        print("Deleting Blood with the ID: ", bID)

        sql_delete_query = """delete from Blood where HospitalID = %s and BloodType = %s and RequestDate = %s"""
        cursor.execute(sql_delete_query, (rbhHospitalID, rbhBloodType, rbhRequestDate))
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully deleted from Blood table...")
        return 1
    except (Exception, psycopg2.Error) as error:
        print("Error deleting record from Blood:", error)
        return 0
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#---------------------------------------------------------------
#Return values:
#1: Deleted from table
#0: Database error -> not deleted