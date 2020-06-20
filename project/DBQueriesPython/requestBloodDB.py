import psycopg2
from DBQueriesPython.databaseInfo import user, password, host, port, database

def requestBloodDB(requestedType, requestedAmount):
    try:
        connection = psycopg2.connect(user = user,
                                      password = password,
                                      host = host,
                                      port = port,
                                      database = database)

        cursor = connection.cursor()

        sql_select_query = """select * from BloodGroup where Type = %s"""
        cursor.execute(sql_select_query, (requestedType,))
        data = cursor.fetchall()
        if not data:
            print("That kind of blood does not exist");
            status = 0
        else:
            sql_select_query = """select * from BloodGroup where Type = %s and TotalAmount >= %s"""
            cursor.execute(sql_select_query, (requestedType, requestedAmount))
            data = cursor.fetchall()

            get_current_amount_query = """select TotalAmount from BloodGroup where Type = %s"""
            cursor.execute(get_current_amount_query, (requestedType,))
            current_amount = cursor.fetchone()[0]
            # print(current_amount)
            if not data:
                print("Not enough ", requestedAmount, "(ml) blood of blood type ", requestedType, "! Still taking all...");
                sql_update_query = """update BloodGroup set TotalAmount = 0 where Type = %s"""
                cursor.execute(sql_update_query, (requestedType,))
                connection.commit()
                status = 0
            else:
                print("There's enough ", requestedAmount, "(ml) blood of blood type ", requestedType, "!");
                updated_amount = current_amount - requestedAmount
                sql_update_query = """update BloodGroup set TotalAmount = %s where Type = %s"""
                cursor.execute(sql_update_query, (updated_amount, requestedType))
                connection.commit()
                print("There's", updated_amount, "(ml) of blood group", requestedType, "remain.")
                status = 1

        return status
    except (Exception, psycopg2.Error) as error:
        print("Error while processing bloodRequest from Hospital:", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#requestBloodDB("O+",4)