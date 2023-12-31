from flask import Flask, request, redirect, Response, Response
import flask
from dotenv import load_dotenv
import os
from DBConnector import execute_query, execute_query_commit
import json
from datetime import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['CORS_SUPPORTS_CREDENTIALS'] = True
CORS(app,  support_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)
def hello_world():
    return "<h1> Hello World </h1>"

@app.route("/customer/<user_id>/purchases", methods=['GET'])
@cross_origin(supports_credentials=True)
def customer_purchases(user_id):
    if request.method == 'GET':
        query = '''
                SELECT user_token, course_cms_id FROM Purchases WHERE user_token = %s;
                '''
        vars = (user_id,)
        result = execute_query(query, vars)

        resp = Response(json.dumps(result), mimetype='text/html')
        # resp.headers.add('Access-Control-Allow-Headers', '*')
        # resp.headers.add('Access-Control-Allow-Origin', '*')
        # resp.headers.add('Access-Control-Allow-Methods', '*')

        return resp
    
@app.route("/customer/<user_id>/reviews", methods=['GET'])
@cross_origin(supports_credentials=True)
def customer_reviews(user_id):
    if request.method == 'GET':
        query = '''
                SELECT user_token, cms_id, review_score FROM reviews WHERE user_token = %s;
                '''
        vars = (user_id,)
        result = execute_query(query, vars)

        resp = Response(json.dumps(result), mimetype='text/html')
        # resp.headers.add('Access-Control-Allow-Headers', '*')
        # resp.headers.add('Access-Control-Allow-Origin', '*')
        # resp.headers.add('Access-Control-Allow-Methods', '*')

        return resp


@app.route('/purchases', methods=['POST'])
@cross_origin(supports_credentials=True)
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

        resp = Response("Purchase successful", 201)
        # resp.headers.add('Access-Control-Allow-Headers', '*')
        # resp.headers.add('Access-Control-Allow-Origin', '*')
        # resp.headers.add('Access-Control-Allow-Methods', '*')
        return resp
        

@app.route("/reviews", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_product_reviews():
    if request.method == 'GET':
        query = '''
                SELECT cms_id AS course_cms_id, AVG(review_score) AS review_score
                FROM Reviews
                GROUP BY (cms_id);
                '''
        result = execute_query(query)
        resp = Response(json.dumps(result), mimetype='text/html')
        # resp.headers.add('Access-Control-Allow-Headers', '*')
        # resp.headers.add('Access-Control-Allow-Origin', '*')
        # resp.headers.add('Access-Control-Allow-Methods', '*')

        return resp
    

    elif request.method == 'POST':
        query = '''
                INSERT INTO Reviews (cms_id, user_token, review_score)
                VALUES (%s, %s, %s)
                '''
        json_body = request.get_json()

        vars = (json_body['cms_id'],json_body['user_token'], json_body['review_score'])

        execute_query_commit(query, vars)

        resp = Response("Review successful", 201)
        # resp.headers.add('Access-Control-Allow-Headers', '*')
        # resp.headers.add('Access-Control-Allow-Origin', '*')
        # resp.headers.add('Access-Control-Allow-Methods', '*')
        return resp


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' )

