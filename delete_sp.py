def delete(table, msg):    
    msg += f"""
    @Id{table[:-1]} int"""

    msg += f"""
AS
BEGIN TRY

    DELETE FROM [dbo].[{table}]
    WHERE [Id{table[:-1]}] = @Id{table[:-1]};

END TRY 

BEGIN CATCH

    SELECT ERROR_MESSAGE() AS Response;

END CATCH
"""
    return msg