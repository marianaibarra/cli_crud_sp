def update(fullColumns, table, msg):
    # TODO:
    # - TAKE OUT None type (dont write it)
    # - Put primary key at bottom and dont add comma
    
    # 0. Column Name
    # 1. Datatype
    # 2. charmaxlenght  
    for i in fullColumns:
        if i[2] == "None":
            i[0] = ""
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
    UPDATE [dbo].[{table}]
    SET """
    for i in fullColumns:
        msg += f"""[{i[0]}] = [@{i[0]}],
    """

    msg += f"""

    WHERE [Id{table[:-1]}] = @Id{table[:-1]};

END TRY 

BEGIN CATCH

    SELECT ERROR_MESSAGE() AS Response;

END CATCH
"""
    return msg