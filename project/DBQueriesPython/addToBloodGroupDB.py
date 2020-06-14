import psycopg2

def addToBloodGroup (bgBloodType, bgAddedAmount):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()

        cursor.execute("""select TotalAmount from BloodGroup where BloodType = %s""", (bgBloodType,))
        current_amount = cursor.fetchone()[0]
        current_amount += bgAddedAmount

        print("Adding into blood group: ",bgBloodType,"~",bgAddedAmount)
        cursor.execute("""update BloodGroup set TotalAmount = %s where BloodType = %s""", (current_amount, bgBloodType))
        connection.commit()

        count = cursor.rowcount
        print(count, "records sucessfully inserted into BloodGroup table")

    except(Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into BloodGroup table: ", error)
    finally:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


# bgBloodType = "O-"
# bgTotalAmount = 2
# addToBloodGroup(bgBloodType, bgTotalAmount)