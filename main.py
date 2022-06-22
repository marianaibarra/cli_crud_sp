import sys
import pyodbc
import insert_sp

path = sys.argv[1]
nameOfFile = sys.argv[2]
table = sys.argv[3]
typeOfQuery = sys.argv[4]

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-2HVAQE28;'
                      'Database=Inv3;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# Structure query =>
# 0. DBname
# 1. TableSchema
# 2. TableName
# 3. ColumnName
# 4. OrdinalPosition
# 5. ColumnDefault
# 6. IsNullable 
# 7. DataType 
# 8. CharMaxLength
cursor.execute(f'SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N\'{table}\'')

msg = f"CREATE PROCEDURE [dbo].[{nameOfFile[:-4]}]"

fullColumns = []
helper = False

for i in cursor:
    a = i[3]
    b = i[7]
    c = i[8]
    fullColumns.append([a,b,c])

if typeOfQuery == "insert":
    helper = True
    msg = insert_sp.insert(fullColumns, table, msg)
elif typeOfQuery == "get":
    helper = True
    # msg = get_sp.get()
    msg = "get"
elif typeOfQuery == "getone":
    helper = True
    # msg = get_one_sp.getOne()
    msg = "getone"
elif typeOfQuery == "update":
    helper = True
    # msg = update_sp.update()
    msg = "update"
elif typeOfQuery == "delete":
    helper = True
    # msg = delete_sp.delete()
    msg = "delete"

if helper:
    try:
        with open(nameOfFile, 'w') as f:
            f.write(msg)
    except FileNotFoundError:
        print(f"The {path} path directory does not exist")
