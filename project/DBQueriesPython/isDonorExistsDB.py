import psycopg2
from databaseInfo import user, password, host, port, database
'''
NOTE:   Currently not used
'''
def isDonorExists(donPerID, cursor):
    try:
        sql_select_query = """select * from Donor where PersonalID = %s"""
        cursor.execute(sql_select_query, (donPerID,))
        #data = cursor.fetchall()

        data = cursor.fetchone() #khong can dung den fetchall vi chi kiem tra co ton tai hay k

        #print(data)
        if not data:
            print("Donor", donPerID, "does not exist!")
            return 0
        else:
            print("Donor", donPerID, "existed!")
            return 1

    except (Exception, psycopg2.Error) as error:
        print("Error while checking if the donor ever donated", error)
