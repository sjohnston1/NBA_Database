# DDL Queries

create_schema_nba = ('''CREATE SCHEMA IF NOT EXISTS NBA;''')
create_schema_nba_landing = ('''CREATE SCHEMA IF NOT EXISTS NBA_LANDING;''')
create_table_nba_landing_nba_player_data = ('''CREATE TABLE IF NOT EXISTS NBA_LANDING.NBA_PLAYER_DATA (
_id varchar(50)
,birthDate varchar(50)
,birthPlace varchar(100)
,career_AST varchar(50)
,"career_FG%" varchar(50)
,"career_FG3%" varchar(50)
,"career_FT%" varchar(50)
,career_G varchar(50)
,career_PER varchar(50)
,career_PTS varchar(50)
,career_TRB varchar(50)
,career_WS varchar(50)
,"career_eFG%" varchar(50)
,college varchar(150)
,draft_pick varchar(50)
,draft_round varchar(50) 
,draft_team varchar(50)
,draft_year varchar(50)
,height varchar(10)
,highSchool varchar(150)
,name varchar(150)
,position varchar(150)
,shoots varchar(20)
,weight varchar(10));''')

create_table_nba_landing_nba_salary_data = ('''CREATE TABLE IF NOT EXISTS NBA_LANDING.NBA_SALARY_DATA (
league varchar(150)
,player_id varchar(50)
,salary varchar(150)
,season varchar(150)
,season_end varchar(150)
,season_start varchar(150)
,team varchar(150));''')
# DML Queries

nba_select = ('''SELECT * FROM INFORMATION_SCHEMA.COLUMNS;''')
nba_select_nba_landing_nba_player_data = ('''SELECT * FROM NBA_LANDING.NBA_PLAYER_DATA;''')

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
create_table_nba_landing_nba_salary_data = SQLCreateTable(create_table_nba_landing_nba_salary_data)
nba_select_nba_landing_nba_player_data_query = SQLSelect(nba_select_nba_landing_nba_player_data)