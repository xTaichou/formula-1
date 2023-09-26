import pyodbc
import pandas as pd
import numpy

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=matt-lenovo\sqlexpress;Database=Formula1;uid=TestAccount;pwd=Testing@1;Trusted_Connection=yes;')

d = {'col1': [1, 2], 'col2': ['name', 'test']}
test = pd.DataFrame(data=d)


cursor = cnxn.cursor()
try:
    df = pd.read_sql_query("SELECT top 1 * FROM results where position = '1' order by raceId desc", cnxn)

    print(test.iat[0])
except pyodbc.ProgrammingError:
    print('Table does not exist')
    cursor.execute("create table test(id int PrimAry Key, name varchar(50))")
    cnxn.commit()
    exit(0)

