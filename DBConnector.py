import psycopg2, psycopg2.extras
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_URL')
port=os.getenv('DB_PORT')
database = os.getenv('DB_NAME')


def connect():

    #Create a connection object.
    conn = psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=host,
        port=port,
    )

    # conn = mysql.connector.connect(
    #     database=database,
    #     user=username,
    #     password=password,
    #     host=host,
    #     port=port,
    # )

    return conn

def execute_query(query, vars=None):
    conn = connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    # cur = conn.cursor(dictionary=True)
    cur.execute(query, vars=vars)
    # cur.execute(query, vars)

    # Fetch the results.
    rows = cur.fetchall()
    
    conn.close()
    return rows

def execute_query_commit(query, vars):
    conn = connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    # cur = conn.cursor(dictionary=True)
    # cur.execute(query, vars)
    cur.execute(query, vars=vars)
        
    conn.commit()
    conn.close()
    


# print(execute_query("SELECT * FROM COURSES WHERE course_id = %s", (1,)).dict())

