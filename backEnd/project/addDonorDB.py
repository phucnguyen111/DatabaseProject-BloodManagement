import psycopg2

def addDonor(donName, donGender, donAddress, donEmail, donCont, donBloodGroup, donMedRec):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()


        print("Adding donor: ",donName,"~"+donGender,"~",donAddress,"~",donEmail,"~",donCont,"~",donBloodGroup,"~",donMedRec)

        sql_insert_query = """insert into Donor(Name, Gender, Address, Email, ContactNumber, BloodGroup, MedicalReport) values(%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (donName, donGender, donAddress, donEmail, donCont, donBloodGroup, donMedRec)
        cursor.execute(sql_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully inserted into Donor table...")

    except (Exception, psycopg2.Error) as error:
        print("Error inserting record to Donor:", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

donName = "Hennessy"
donGender = "Male"
donAddress = "Washington D.C."
donEmail = "Henneckbeard@gmail.com"
donCont = "WHS13574768LE"
donBloodGroup = "B-"
donMedRec = "Very strong man, healthy blood"

addDonor(donName, donGender, donAddress, donEmail, donCont, donBloodGroup, donMedRec)