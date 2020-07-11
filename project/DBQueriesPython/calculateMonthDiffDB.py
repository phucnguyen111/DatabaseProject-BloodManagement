import psycopg2
from DBQueriesPython.databaseInfo import user, password, host, port, database

'''
This function checks for the donor's last donation to see whether he/she is qualified for the next donation
@param[in]:     donPerID            Donor's personal ID

@return:        status              The time interval between the last donation and this current one
                time                valid time
                -1                  Invalid time
                -2                  Donor does not exist
'''


def calculateMonthDiff(donPerID):
    try:
        connection = psycopg2.connect(user = user,
                                      password = password,
                                      host = host,
                                      port = port,
                                      database = database)
        cursor = connection.cursor()

        cursor.execute("""select PersonalID from Blood where PersonalID = %s""", (donPerID,)
                        )  # Phai dung PersonalID o bang Blood ma khong dung bang Donor vi neu nguoi
                                                                                                # hien lan dau da duoc them vao bang donor -> is_donor_exist is not None
                                                                                                # -> jump to else -> tuy nhien, trong bang blood van chua co PersonalID cua
        latest_date = "None"                                                                                        # nguoi nay -> sql_get_latest_date_query se tra ve None
        is_donor_exist = cursor.fetchone()
           # print(is_donor_exist)
        if is_donor_exist is None:
            return (-2, latest_date)
        else:
            sql_get_latest_date_query = """select max(DonationDate) from Blood where Blood.PersonalID = %s"""
            cursor.execute(sql_get_latest_date_query, (donPerID,))
            # cursor.fetchone se return dang tuple, vi select max nen tuple chi co mot phan tu -> lay phan tu tuple[0
            latest_date = cursor.fetchone()[0]
            print("Latest donated: ", latest_date)
            get_month_diff_query = """select (date_part('year', timestamp 'NOW()')-date_part('year', timestamp %s))*12+date_part('month', timestamp 'NOW()') - date_part('month',timestamp %s)"""
            cursor.execute(get_month_diff_query,(latest_date, latest_date))
            month_difference = cursor.fetchone()[0]
            print("The month difference interval:", month_difference)
            return (month_difference, latest_date)
    except (Exception, psycopg2.Error) as error:
        print("Error while calculating difference in months: ", error)
        return (-1, latest_date)
    finally:
        if (connection):
            cursor.close()
            connection.close()

# print(calculateMonthDiff(123456))

# ---------------------------------------------------------------
# Return values:
# month_difference: the month difference interval which is calculated successfully
# -1: Database error -> Could not calculated
# -2: Donor does not exist!
