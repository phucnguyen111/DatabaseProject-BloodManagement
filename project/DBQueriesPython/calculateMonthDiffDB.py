import psycopg2


'''
This function checks for the donor's last donation to see whether he/she is qualified for the next donation
@param[in]:     donPerID            Donor's personal ID

@return:        status              The time interval between the last donation and this current one
                time                valid time
                -1                  Invalid time
'''
def calculateMonthDiff (donPerID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="ha3171999",
                                      host="localhost",
                                      port="5432",
                                      database="BloodBank")
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
