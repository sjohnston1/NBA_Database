import psycopg2
from psycopg2 import Error
import sys
from db_credentials import *
from sql_queries import *
from io import StringIO
import pandas

debug = 0

source_db_config = ''
source_db_name = ''

target_db_config = nba_database_config
target_db_name = nba_database_name

memory_buffer = None
player_data_frame = None

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
        #function you want to run goes here

        memory_buffer = StringIO()

        cursor.copy_expert('''COPY (SELECT a.name, a.draft_team FROM (SELECT name, draft_team, draft_year 
        FROM NBA_LANDING.NBA_PLAYER_DATA WHERE TRIM(draft_year) NOT IN ('1st', '2nd', '8th') ) AS a
        WHERE cast(a.draft_year as integer) > 2003) 
        TO STDIN WITH CSV HEADER DELIMITER '|';''', memory_buffer)

        memory_buffer.seek(0)

        player_data_frame = pandas.read_csv(memory_buffer, sep='|')
        
        #select *
        #print(player_data_frame.to_string())
        
        #prints out specific column, kinda like select coulmn
        #print(player_data_frame[['name']])

        #prints out the value from ids x:y
        #print(player_data_frame.loc[0:100,['name']])

        #prints out the info for a value
        #print(player_data_frame.loc[0,:])
        
        #adding a value based on another column, kinda like a case statement
        '''def if_team(teamname):
            if teamname == 'Portland Trail Blazers':
                return 'hype'
            else:
                return 'boo'
        
        player_data_frame['Like_team'] = player_data_frame['draft_team'].map(if_team)

        print(player_data_frame.to_string())'''
        
        #prints out for x value, similar to where value        
        #print(player_data_frame[player_data_frame['draft_team'] == 'Portland Trail Blazers'])

        #where is similar to sql where, but doesn't filter out nulls/nas. Need to use dropna()
        '''filter = player_data_frame['draft_team'] == 'Portland Trail Blazers'
        filter2 = player_data_frame['draft_team'] == 'Milwaukee Bucks'

        player_data_frame.where(filter | filter2,inplace=True)

        print(player_data_frame.dropna().to_string())'''

    except (Exception, Error) as sql_error:
        print(sql_error)
        if connection:
            connection.close()
            print("Successful disconnection from the database", target_db_name)
            sys.exit()

    if connection:
            connection.close()
            print("Successful disconnection from the database", target_db_name)