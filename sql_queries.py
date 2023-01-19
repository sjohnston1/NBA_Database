# DDL Queries

create_schema = ('''CREATE SCHEMA NBA;''')
create_table = ('''CREATE TABLE NBA.NBA;''')

# DML Queries

nba_select = ('''SELECT * FROM INFORMATION_SCHEMA.COLUMNS;''')



class SQLSelect:
    def __init__(self,select_query):
        self.select_query = select_query

class SQLCreateTable:
    def __init__(self,create_table):
        self.create_table = create_table

class SQLCreateSchema:
    def __init__(self,create_schema):
        self.create_schema = create_schema

nba_select_query = SQLSelect(nba_select)
