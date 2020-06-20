import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "NVHplay.99.02.21",
                                  host = "localhost",
                                  port = "9221",
                                  database = "BloodDonateProject")

    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")