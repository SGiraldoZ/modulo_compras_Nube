from flask import Flask, request, redirect, Response
import flask
from dotenv import load_dotenv
import os
from DBConnector import execute_query, execute_query_commit
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Hello World </h1>"

@app.route("/customer/<user_id>/purchases", methods=['GET'])
def customer_purchases(user_id):
    if request.method == 'GET':
        query = '''
                SELECT * FROM Purchases WHERE user_token = %s;
                '''
        vars = (user_id,)
        result = execute_query(query, vars)

        return json.dumps(result)


@app.route('/purchases', methods=['POST'])
def post_purchase():
    if request.method == 'POST':
        query = '''
                INSERT INTO purchases (user_token, course_cms_id, price, purchase_date)
                VALUES (%s,%s,%s,%s);
                '''
        p_date = datetime.now()
        json_body = request.get_json()
        vars = (json_body['user_token'], json_body['course_id'], json_body['purchase_price'], p_date)
        execute_query_commit(query, vars)

        return Response('Purchase Successful!',201)
        

@app.route("/reviews", methods=['GET'])
def get_product_reviews():
    query = '''
            SELECT cms_id AS course_cms_id, AVG(review_score) AS review_score
            FROM reviews
            GROUP BY (cms_id);
            '''
    result = execute_query(query)
    return json.dumps(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' )

