def open_connector():
    import pymysql

    conn = pymysql.connect(
    host='localhost',
    user='hooniegit',
    passwd='1234',
    database='spotify'
    )

    return conn


def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()


def fetchall_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    return result