


def get_products(connection):
    cursor = connection.cursor()
    query = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit,uom.uom_name FROM Grocery_Store.products inner join Grocery_Store.uom on products.uom_id = uom.uom_id;"
    cursor.execute(query)
    response =[]
    for(product_id, name, uom_id, price_per_unit,uom_name) in cursor:
        response.append({
            'product_id' : product_id,
            'name' : name,
            'uom_id' : uom_id,
            'price_per_unit' : price_per_unit,
            'uom_name' : uom_name
        })

    return response

def insert_new_products(connection,products):
    cursor = connection.cursor()
    query = "Insert into Grocery_Store.products(name,uom_id,price_per_unit) values(%s,%s,%s) ;"
    data = (products['product_name'],products['uom_id'],products['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid


def delete_products(connection,product_id):
    cursor = connection.cursor()
    query = "Delete from Grocery_Store.products where product_id = " + str(product_id)
    cursor.execute(query)
    connection.commit()
