import psycopg2
from psycopg2 import Error
import sys
from db_credentials import *
from sql_queries import *

debug = 0

source_db_config = ''
source_db_name = ''

target_db_config = nba_database_config
target_db_name = nba_database_name

try :
    connection = psycopg2.connect(
        target_db_config
    )

    cursor = connection.cursor()

    print("Successful connection to the database", target_db_name)

except(Exception, Error) as connection_error:
    print("Error while connecting to the database", target_db_name)
    print(connection_error)
    if debug == 1:
        raise
        print("debug!")
    sys.exit()

else :
    try :
        cursor.execute(create_schema_nba.create_schema)
        connection.commit();
    
    except (Exception, Error) as sql_error:
        print(sql_error)
        if connection:
            connection.close()
            print("Successful disconnection from the database", target_db_name)
            sys.exit()

    if connection:
            connection.close()
            print("Successful disconnection from the database", target_db_name)