import aiopg.sa
import psycopg2

#__all__ = ['Donor', 'Blood', 'Hospital', 'BloodDonateProject', 'Donor_Donate_Blood',
#           'Blood_Belongs_To_BloodDonateProject', 'BloodDonateProject_ManageInfo_Donor', 'BloodDonateProject_DistributeBlood_Hospital']

async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database = conf['database'],
        user = conf['user'],
        password = conf['password'],
        host = conf['host'],
        port = conf['port'],
        minsize = conf['minsize'],
        maxsize = conf['maxsize']
    )
    app['db'] = engine

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()

'''
This function is to create new donor
NOTE: Need to be moved to DBQueries
'''
def create_donor(name, gender, address, email, contact, bloodgroup, medicalRecord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="NVHplay.99.02.21",
                                      host="localhost",
                                      port="9221",
                                      database="BloodDonateProject")
        cursor = connection.cursor()


        print("Adding donor: " + name +  "~" + gender + "~" + address + "~" + email + "~" + contact + "~" + bloodgroup + "~" + medicalRecord)

        sql_insert_query = """insert into Donor(Name, Gender, Address, Email, ContactNumber, BloodGroup, MedicalReport) values(%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (name, gender, address, email, contact, bloodgroup, medicalRecord)
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


def delete_donor(donID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="NVHplay.99.02.21",
                                      host="localhost",
                                      port="9221",
                                      database="BloodDonateProject")
        cursor = connection.cursor()

        print("Deleting donor with the ID: ", donID)

        sql_insert_query = """delete from Donor where DonorID = %s"""
        cursor.execute(sql_insert_query, (donID,))
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully deleted from Donor table...")

    except (Exception, psycopg2.Error) as error:
        print("Error deleting record from Donor:", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
