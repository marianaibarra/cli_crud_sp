def insert(fullColumns, table, msg):
    # TODO:
    # - TAKE OUT None type (dont write it)
    # - Put primary key at bottom and dont add comma
    
    # 0. Column Name
    # 1. Datatype
    # 2. charmaxlenght  
    for i in fullColumns:
        if i[2] == "None":
            i[0] = ""
        if(i[0] == "Id" + table[:-1]):
            i[1] = " int = 0 output"
        msg += f"""
    @{i[0]} {i[1]}({i[2]}),"""

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
    for i in fullColumns:
        msg += f"[{i[0]}],"

    msg += """)
    VALUES ("""
    # TODO:
    # - Take primary key out of here
    # - dont add comma on last field
    for i in fullColumns:
        msg += f"[@{i[0]}],"

    msg += f""")

    SELECT @Id{table[:-1]} = SCOPE_IDENTITY();

END TRY 

BEGIN CATCH

    SELECT ERROR_MESSAGE() AS Response;

END CATCH
"""
    return msg