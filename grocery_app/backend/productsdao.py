def check_user(connection, user_details, password):
    cursor = connection.cursor()
    user_details = str(user_details).strip()
    if user_details.isdigit():
        cursor.execute(
            "Select 1,id from users where id = %s and password = %s limit 1",
            (int(user_details), password),
        )
    else:
        cursor.execute(
            "Select 1,id from users where user_name = %s and password = %s limit 1",
            (user_details, password),
        )
    response = []
    for rows, user_id in cursor:
        response.append({"row": rows, "user_id": user_id})
    connection.close()
    return response


def insert_users(connection, user_name, email, password):
    cursor = connection.cursor()
    query = (
        "Insert into Grocery_Store.users(user_name,email,password) values(%s,%s,%s);"
    )
    cursor.execute(query, (user_name, email, password))
    connection.commit()
    connection.close()
    return "Your profile is created successfully"


def get_products(connection):
    cursor = connection.cursor()
    query = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit,uom.uom_name FROM Grocery_Store.products inner join Grocery_Store.uom on products.uom_id = uom.uom_id;"
    cursor.execute(query)
    response = []
    for product_id, name, uom_id, price_per_unit, uom_name in cursor:
        response.append(
            {
                "product_id": product_id,
                "name": name,
                "uom_id": uom_id,
                "price_per_unit": price_per_unit,
                "uom_name": uom_name,
            }
        )
    connection.close()
    return response


def insert_new_products(connection, products):
    cursor = connection.cursor()
    query = "Insert into Grocery_Store.products(name,uom_id,price_per_unit) values(%s,%s,%s) ;"
    data = (products["name"], products["uom_id"], products["price_per_unit"])
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return "Your products are created successfully. Please view in manage products"


def delete_products(connection, product_id):
    cursor = connection.cursor()
    query = "Delete from Grocery_Store.products where product_id = " + str(product_id)
    cursor.execute(query)
    connection.commit()
    connection.close()
    return "Product deleted successfully"
