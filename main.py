import sys
import pyodbc

path = sys.argv[1]
nameOfFile = sys.argv[2]
table = sys.argv[3]
typeOfQuery = sys.argv[3]

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

columsNames = []
# TODO:
# - TAKE OUT None type (dont write it)
# - Put primary key at bottom and dont add comma
# - Wrap in brackets CharMaxLength 
for i in cursor:

    a = i[3]
    b = i[7]
    c = i[8]
    if c == "None":
        a = None
    if(i[3] == "Id" + table[:-1]):
        b = " int = 0 output"
    msg += f"""
    @{a} {b} {c},"""
    columsNames.append(i[3])


msg += """
AS
BEGIN TRY
SET NOCOUNT ON;
"""
# TODO:
# - Take primary key out of here
# - dont add comma on last field
msg += f"""
INSERT INTO [dbo].[{table}]
("""
for i in columsNames:
    msg += f"[{i}],"

msg += """)
    VALUES ("""
# TODO:
# - Take primary key out of here
# - dont add comma on last field
for i in columsNames:
    msg += f"[@{i}],"

msg += f""")

    SELECT @Id{table[:-1]} = SCOPE_IDENTITY();

END TRY 

BEGIN CATCH

    SELECT ERROR_MESSAGE() AS Response;

END CATCH
"""

try:
    with open(nameOfFile, 'w') as f:
        f.write(msg)
except FileNotFoundError:
    print(f"The {path} path directory does not exist")
