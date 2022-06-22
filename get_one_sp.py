def getOne(fullColumns, table, msg):
    msg += f"""
    
AS
BEGIN TRY

    SET NOCOUNT ON;
    """
    msg += f"""
    SELECT """
    for i in fullColumns:
        msg += f"[{i[0]}],"
    msg += f"""
    FROM [dbo].[{table}]
    WHERE [Id{table[:-1]}] = @Id{table[:-1]};

END TRY 

BEGIN CATCH

    SELECT ERROR_MESSAGE() AS Response;

END CATCH
"""
    return msg