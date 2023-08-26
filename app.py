from flask import Flask, request
from dotenv import load_dotenv
import os
from DBConnector import execute_query
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/customer/<user_id>/purchases.json", methods=['GET', 'POST'])
def customer_purchases(user_id):
    if request.method == 'GET':
        query = '''
                SELECT u.u_id, c.course_name, c.cms_id
                FROM users AS u LEFT  JOIN purchases AS p ON u.u_id = p.u_id
                LEFT  JOIN courses AS c ON c.course_id = p.course_id
                WHERE u.token = %s;
                '''
        vars = (user_id,)
        result = execute_query(query, vars)

        return json.dumps(result)
    
    elif request.method == 'POST':
        query = '''
                INSERT INTO purchases (u_id, course_id, price, purchase_date)
                VALUES (SELECT u_id FROM users WHERE token = %s;,'%s','%s','%s');
                '''
        p_date = datetime.now()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' )

