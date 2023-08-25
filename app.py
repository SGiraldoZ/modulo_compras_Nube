from flask import Flask
from dotenv import load_dotenv
import os
from DBConnector import execute_query
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/customer/<user_id>/purchases.json")
def customer_purchases(user_id):
    query = '''
            SELECT u.u_id, c.course_name, c.cms_id
            FROM users AS u LEFT  JOIN purchases AS p ON u.u_id = p.u_id
            LEFT  JOIN courses AS c ON c.course_id = p.course_id
            WHERE u.token = %s'''
    vars = (user_id,)
    result = execute_query(query, vars)

    return json.dumps(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' )

