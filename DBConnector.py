import psycopg2, psycopg2.extras
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_URL')
port=os.getenv('DB_PORT')


def connect():

    # Create a connection object.
    conn = psycopg2.connect(
        database="udemy",
        user=username,
        password=password,
        host=host,
        port=port,
    )

    return conn

def execute_query(query, vars):
    conn = connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(query, vars=vars)

    # Fetch the results.
    rows = cur.fetchall()
    
    conn.close()
    return rows


# print(execute_query("SELECT * FROM COURSES WHERE course_id = %s", (1,)).dict())

