def open_connector():
    import pymysql

    conn = pymysql.connect(
    host='localhost',
    user='hooniegit',
    passwd='1234',
    database='spotify'
    )

    return conn


# def execute_query(conn, query):
#     cursor = conn.cursor()
#     cursor.execute(query)
#     conn.commit()
#     cursor.close()


def execute_query(conn, query, values):
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()


def fetchall_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    return result


if __name__ == "__main__":

    from datetime import datetime
    nowdate = datetime.now().strftime("%Y-%m-%d")
    print(nowdate)
    conn = open_connector()
    query_search = f"""
                   SELECT id FROM albums
                   WHERE insert_date = '{nowdate}';
                   """
    result = fetchall_query(conn=conn, query=query_search)
    print(result)
    conn.close()