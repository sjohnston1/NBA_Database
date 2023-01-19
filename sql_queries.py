# DDL Queries

create_schema_nba = ('''CREATE SCHEMA IF NOT EXISTS NBA;''')
create_table_nba_salary = ('''CREATE TABLE NBA.NBA;''')

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
create_table_nba_salary = SQLCreateTable(create_table_nba_salary)