from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from flasgger import Swagger

app = Flask("Product Server")
CORS(app)
swagger = Swagger(app)

products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

#
# Example request - http://127.0.0.1:5000/products
@app.route('/products', methods=['GET'])
def get_products():
    """
    Get all products
    ---
    tags:
      - Products
    responses:
      200:
        description: List of products
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              price: 
                type: number
                format: float
    """
    return jsonify(products)

# Example request - http://127.0.0.1:5000/products/144 - with method GET
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    return jsonify(product)

# Example request - http://127.0.0.1:5000/products - with method POST
@app.route('/products', methods=['POST'])
def add_product():
    """
    Create a new product
    ---
    tags:
      - Products
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
          properties:
            id:
              type: integer
            name:
              type: string
            price:
              type: number
              format: float
    responses:
      201:
        description: Product created
    """
    products.append(request.get_json())
    return '', 201

# Example request - http://127.0.0.1:5000/products/144 - with method PUT
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    """
    Update a product
    ---
    tags:
      - Products
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: The ID of the item
      - in: body
        name: body
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            price:
              type: number
              format: float
    responses:
      204:
        description: Product updated
      404:
        description: Product not found
    """
    id = int(id)
    updated_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in updated_product.items():
        product[key] = value
    return '', 204

# Example request - http://127.0.0.1:5000/products/144 - with method DELETE
@app.route('/products/<int:id>', methods=['DELETE'])
def remove_product(id):
    """
    Delete a product
    ---
    tags:
      - Products
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: The ID of the product
    responses:
      204:
        description: Product deleted
      404:
        description: Product not found
    """
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '', 204

app.run(port=5000,debug=True)