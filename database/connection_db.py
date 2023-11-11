import pymysql

R = '\033[31m'  # Red
G = '\033[32m'  # Green
RS = '\033[39m'  # Reset


def connect_db():
    """
    Connect to database.
    """

    connection = {}
    params = {
        "host": "localhost",
        "user": "root",
        "password": "syllabus",
        "database": "syllabus",
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor
    }

    try:
        connection = pymysql.connect(**params)
        print(f"{G} * Connection to MySQL instance succesfully.{RS}")

    except Exception as e:
        print(f"{R} * Couldn't connect to MySQL instance: {RS}", e)

    return connection


def execute_query(query, rw=False):
    """
    execute_query
    ---

    The method receives a query it is in SQL and its gonna be executed.

    params:
    * query: The query on SQL.
    * rw: Read & Write. False -> Select. True -> Insert, Update, Delete. 
    """

    # SELECT.
    conn = connect_db()
    data = {}

    print(f"Query executing: {query}\n")
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)

            if not rw:
                data = cursor.fetchall()

            else:
                conn.commit()
                data = cursor.lastrowid

        print(f"{G} *The query has been executed successfully.{RS}")

    except Exception as e:
        print(f'{R} * ERROR: Couldnt connect to the database.\n{RS} {e}')
    
    return data
