import productsdao
from flask import Flask, jsonify, request
from sql_connection import get_sql_connection

app = Flask(__name__)


@app.route("/product", methods=["GET","POST","DELETE"])
def product():
    if request.method == 'GET':
        products = productsdao.get_products(get_sql_connection())
        response = jsonify(products)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    elif request.method == 'POST':
        data = request.get_json()
        products = {
            'name' : data.get("name") ,
            'uom_id' : data.get("uom_id"),
            'price_per_unit' : data.get("price_per_unit")
        }
        output = productsdao.insert_new_products(get_sql_connection(),products)
        return jsonify({
            "Message" : output
        })
    elif request.method == "DELETE":
        id = request.get_json()
        output = productsdao.delete_products(get_sql_connection(),id.get('id'))
        return jsonify({
            "Message" : output
        })


@app.route("/user", methods=["GET"])
def user():
    if request.method == 'GET':
        user = request.args.get("user")
        pword = request.args.get("pword")
        if user is None or pword is None:
            return jsonify(
                {
                    "Error": "User name/Id and Password are required. Please provide to continue"
                }
            ), 400
        users = productsdao.check_user(get_sql_connection(), user, pword)
        return jsonify(users)
    elif request.method == 'POST':
        data = request.get_json()
        user_name = data.get("user_name")
        password = data.get("password")
        email = data.get("email")
        if (not user_name) or (not password) or (not email):
            return jsonify(
                {
                    "Error": "One of the required fields is empty. Please provide information to continue"
                }
            ), 400
        output = productsdao.insert_users(get_sql_connection(), user_name, email, password)
        return jsonify({"Message": output})

if __name__ == "__main__":
    print("starting python")
    app.run(port=5500)
