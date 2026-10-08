import productsdao
from flask import Flask, jsonify, request
from sql_connection import get_sql_connection

app = Flask(__name__)


@app.route('/get_products', methods = ['GET'])
def get_products():
    products = productsdao.get_products(get_sql_connection())
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("starting python")
    app.run(port=5000)
