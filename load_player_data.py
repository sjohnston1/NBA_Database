import psycopg2
from psycopg2 import Error
import sys
from db_credentials import nba_database_config, nba_database_name
from sql_queries import *
import pandas
from io import StringIO

debug = 0

source_db_config = ''
source_db_name = ''

target_db_config = nba_database_config
target_db_name = nba_database_name

nba_player_data_CSV = None
nba_player_data_frame = None
memory_buffer = None

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
        nba_player_data_CSV = 'C:\\Users\\golfn\\Desktop\\python\\players.csv'
        nba_player_data_frame = pandas.read_csv(nba_player_data_CSV)

        memory_buffer = StringIO()
        nba_player_data_frame.to_csv(memory_buffer, header=True, index=False, sep='|')
        memory_buffer.seek(0)
        
        if debug == 1:
            testprint = memory_buffer.getvalue()
            print(testprint)

        try:
            cursor.copy_expert('''COPY NBA_LANDING.NBA_PLAYER_DATA FROM STDIN WITH CSV HEADER DELIMITER '|';''', memory_buffer)

        except (Exception, Error) as sql_error:
            print(sql_error)
            if connection:
                connection.close()
                print("Successful disconnection from the database", target_db_name)
                sys.exit()

        connection.commit()
    
    
    except (Exception, Error) as sql_error:
        print(sql_error)
        if connection:
            connection.close()
            print("Successful disconnection from the database", target_db_name)
            sys.exit()

    if connection:
            connection.close()
            print("Successful disconnection from the database", target_db_name)