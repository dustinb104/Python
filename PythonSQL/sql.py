import pyodbc as odbc
import pandas as pd
from sqlalchemy import create_engine

server_name = 'DUSTIN-PC\\SQLSERVER25'
database_name = 'master'
driver_name = 'ODBC Driver 17 for SQL Server'

engine = create_engine(f'mssql+pyodbc://{server_name}/{database_name}?driver={driver_name}')

df = pd.read_sql("SELECT * FROM [Post-Katrina_Damage_Assessment]",engine)

print(df.columns)
print(df[['Address','Percentage']].head())