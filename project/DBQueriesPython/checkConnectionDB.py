import psycopg2
from databaseInfo import user, password, host, port, database
try:
    connection = psycopg2.connect(user=user,password=password,host=host,port=port,database=database)
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