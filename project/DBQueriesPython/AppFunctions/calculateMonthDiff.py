import psycopg2

def calculateMonthDiff (donPerID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()
        sql_get_latest_date_query = """select max(DonationDate) 
                                    from Blood 
                                    where Blood.PersonalID = %s"""
        cursor.execute(sql_get_latest_date_query, (donPerID,))
        latest_date = cursor.fetchone()[0]
        print("Latest date that this donor donated: ",latest_date)
        get_month_diff_query = """select (date_part('year', timestamp 'NOW()')-date_part('year', timestamp %s))*12+date_part('month', timestamp 'NOW()') - date_part('month',timestamp %s)"""
        cursor.execute(get_month_diff_query, (latest_date, latest_date))
        month_difference = cursor.fetchone()[0]
        print("The month difference interval:", month_difference)
        return month_difference
    except (Exception, psycopg2.Error) as error:
        print("Error while calculating difference in months: ", error)
        return -1

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

calculateMonthDiff(123456)

#---------------------------------------------------------------
#Return values:
#month_difference: the month difference interval which is calculated successfully
#-1: Database error -> Could not calculated