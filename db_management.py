import pandas as pd
import sqlite3 as sl


def create_initial_table(table_name, df, column_names):
    """creates the basic player stats table if there is a new season.

    Args:
        table_name: (str) name of the table to be created.
        df: (dataframe) initial df from first pull of season.
        column_names: (tuple) list of column names for the table.

    Returns:
        None

    """

    con = sl.connect(r'C:\CODE\learning\Apex_cluster\database\apex.db')

    query = f'Create table if not Exists {table_name}{column_names}'
    con.execute(query)
    df.to_sql(table_name,con,if_exists='replace',index=False)
    con.commit()
    con.close()
    print(f'{table_name} table created')

    return None



def update_table(table_name, df):
    """updates the basic player stats table.

    Args:
        table_name: (str) name of the table to be updated.
        df: (dataframe) dataframe to be appended to table.
    
    Returns:
        None
    
    """
    con = sl.connect(r'C:\CODE\learning\Apex_cluster\database\apex.db')

    df.to_sql(table_name, con, if_exists='append',index=False)
    con.commit()
    con.close()
    print(f'{table_name} table updated')

    return None
