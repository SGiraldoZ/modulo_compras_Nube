from flask import Flask, request, redirect, Response, make_response
import flask
from dotenv import load_dotenv
import os
from DBConnector import execute_query, execute_query_commit
import json
from datetime import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# app.config['CORS_SUPPORTS_CREDENTIALS'] = True
CORS(app)

@app.route("/")
def hello_world():
    return "<h1> Hello World </h1>"

@app.route("/customer/<user_id>/purchases", methods=['GET'])
def customer_purchases(user_id):
    if request.method == 'GET':
        query = '''
                SELECT user_token, course_cms_id FROM Purchases WHERE user_token = %s;
                '''
        vars = (user_id,)
        result = execute_query(query, vars)

        resp = make_response(json.dumps(result))
        resp.headers.add('Access-Control-Allow-Headers', '*')

        return resp
    
@app.route("/customer/<user_id>/reviews", methods=['GET'])
def customer_reviews(user_id):
    if request.method == 'GET':
        query = '''
                SELECT user_token, cms_id, review_score FROM reviews WHERE user_token = %s;
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
        

@app.route("/reviews", methods=['GET', 'POST'])
def get_product_reviews():
    if request.method == 'GET':
        query = '''
                SELECT cms_id AS course_cms_id, AVG(review_score) AS review_score
                FROM reviews
                GROUP BY (cms_id);
                '''
        result = execute_query(query)
        return json.dumps(result)
    elif request.method == 'POST':
        query = '''
                INSERT INTO reviews (cms_id, user_token, review_score)
                VALUES (%s, %s, %s)
                '''
        json_body = request.get_json()

        vars = (json_body['cms_id'],json_body['user_token'], json_body['review_score'])

        execute_query_commit(query, vars)

        return Response("Review successful", 201)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' )

