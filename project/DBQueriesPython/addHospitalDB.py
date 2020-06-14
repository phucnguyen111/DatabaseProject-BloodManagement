import psycopg2

'''
This function is used to populate the addDonor table when donor register blood donation.
'''


def addHospital(hName, hAddress, hEmail, hCont): #hHospitalID de la SERIAL
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()

        print("Adding hospital: ",hName,"~",hAddress,"~",hEmail,"~",hCont)
        sql_insert_query = """insert into Hospital(Name, Address, Email, ContactNumber) values(%s,%s,%s,%s)"""
        record_to_insert = (hName, hAddress, hEmail, hCont)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()

        count = cursor.rowcount
        print(count, "records successfully inserted into Hospital table...")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into Hospital table:", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# hName = "L'Hopital Vietnam et France"
# hAddress = "Phuong Mai, Ha Noi"
# hEmail = "contact@hfh.com.vn"
# hCont = "18EU239DWKKE3"
# addHospital(hName, hAddress, hEmail, hCont)