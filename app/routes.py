from flask import Blueprint, request, jsonify
from app.models import get_db_connection

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Inventory Management System!"

@main.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

@main.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data['name']
    price = data['price']
    stock = data['stock']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product added successfully'})

@main.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product deleted successfully'})

