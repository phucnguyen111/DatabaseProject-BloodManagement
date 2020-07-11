import psycopg2
from databaseInfo import user, password, host, port, database

'''
This function will update the BloodGroup table when a new request comes. It checks from the database to see if the stock can satisfy the request
@param[in]  requestedType       Blood group requested
@param[in]  requestedAmount     Blood amount requested

@return     status              
            0                   Blood type not exist
            1                   Not enough blood
            2                   Enough blood, success
            -1                  Database error

'''
def requestBloodDB(requestedType, requestedAmount):
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()

        sql_select_query = """select * from BloodGroup where BloodType = %s"""
        cursor.execute(sql_select_query, (requestedType,))
        data = cursor.fetchall()
        if not data:
            print("That kind of blood does not exist");

            return 0
        else:
            sql_select_query = """select * from BloodGroup where BloodType = %s and TotalAmount >= %s"""
            cursor.execute(sql_select_query, (requestedType, requestedAmount))
            data = cursor.fetchall()

            get_current_amount_query = """select TotalAmount from BloodGroup where BloodType = %s"""
            cursor.execute(get_current_amount_query, (requestedType,))
            current_amount = cursor.fetchone()[0]
            # print(current_amount)
            if not data:
                print("Not enough ", requestedAmount, "(ml) blood of blood type ", requestedType, "! Still taking all that's left...");
                sql_update_query = """update BloodGroup set TotalAmount = 0 where BloodType = %s"""
                cursor.execute(sql_update_query, (requestedType,))
                connection.commit()

                return 1
            else:
                print("There's enough ", requestedAmount, "(ml) blood of blood type ", requestedType, "!");
                updated_amount = current_amount - requestedAmount
                sql_update_query = """update BloodGroup set TotalAmount = %s where BloodType = %s"""
                cursor.execute(sql_update_query, (updated_amount, requestedType))
                connection.commit()
                print("There's", updated_amount, "(ml) of blood group", requestedType, "remain.")

                return 2

    except (Exception, psycopg2.Error) as error:
        print("Error while processing bloodRequest from Hospital:", error)
        return -1
    # finally:
    #     if (connection):
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")

# print(requestBloodDB("A+",8))

