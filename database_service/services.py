from startup import sql_server 


def execute_query(sql_query):
    try: 
        cursor = sql_server.cursor()
        cursor.execute(sql_query)
        data = cursor.fetchall()
        return data
    except Exception as e: 
        raise Exception(error = "Database Error", msg = f"Error : {e}")
