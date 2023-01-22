# DDL Queries

create_schema_nba = ('''CREATE SCHEMA IF NOT EXISTS NBA;''')
create_schema_nba_landing = ('''CREATE SCHEMA IF NOT EXISTS NBA_LANDING;''')
create_table_nba_landing_nba_player_data = ('''CREATE TABLE NBA_LANDING.NBA_PLAYER_DATA (
_id varchar(50)
,birthDate varchar(50)
,birthPlace varchar(100)
,career_AST numeric(4,2)
,"career_FG%" numeric(4,2)
,"career_FG3%" numeric(4,2)
,"career_FT%" numeric(4,2)
,career_G smallint
,career_PER numeric(4,2)
,career_PTS numeric(4,2)
,career_TRB numeric(4,2)
,career_WS numeric(4,2)
,"career_eFG%" numeric(4,2)
,college varchar(150)
,draft_pick smallint
,draft_round smallint 
,draft_team varchar(50)
,draft_year smallint
,height varchar(10)
,highSchool varchar(150)
,name varchar(150)
,position varchar(150)
,shoots varchar(20)
,weight varchar(10));''')

# DML Queries

nba_select = ('''SELECT * FROM INFORMATION_SCHEMA.COLUMNS;''')

# Class Definitions

class SQLSelect:
    def __init__(self,select_query):
        self.select_query = select_query

class SQLCreateTable:
    def __init__(self,create_table):
        self.create_table = create_table

class SQLCreateSchema:
    def __init__(self,create_schema):
        self.create_schema = create_schema

#Query Setup

nba_select_query = SQLSelect(nba_select)
create_schema_nba = SQLCreateSchema(create_schema_nba)
create_schema_nba_landing = SQLCreateSchema(create_schema_nba_landing)
create_table_nba_landing_nba_player_data = SQLCreateTable(create_table_nba_landing_nba_player_data)