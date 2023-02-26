from flask import request, jsonify, Response
from flask_pymongo import PyMongo  # Necesita: pip install Flask-PyMongo
from bson import json_util
from bson.objectid import ObjectId
from config import app

# Conexión a Mongodb
mongo = PyMongo(app)

@app.route('/products', methods=['POST'])
def create_user():
    # Recibiendo datos
    id = request.json['id']
    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']

    if name and quantity and price:
        mongo.db.products.insert_one({'id': id, 'name': name, 'quantity': quantity, 'price': price})

        response = {
            'id': id,
            'name': name,
            'price': price,
            'quantity': quantity
        }
        return response
    else:
        return not_found()

@app.route('/products', methods=['GET'])
def get_products():
    productos = mongo.db.products.find()
    response = json_util.dumps(productos)  # Strings con formato JSON

    return Response(response, mimetype='application/json') # Formato JSON

@app.route('/products/<id>', methods=['GET'])
def get_user(id):
    producto = mongo.db.products.find_one({'id': id})
    response = json_util.dumps(producto)
    
    return Response(response, mimetype='application/json') # Formato JSON

@app.route('/products/<id>', methods=['DELETE'])
def delete_user(id):
    producto = mongo.db.products.delete_one({'id': id})
    response = jsonify({'mensaje': 'Usuario ' + id + ' fue eliminado satisfactoriamente'})
    
    return response    
    
@app.route('/products/<id>', methods=['PUT'])
def update_user(id):
    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']

    if name and quantity and price:
       
        mongo.db.products.update_one({'id': id}, {'$set': 
        { 
            'name': name,
            'price': price,
            'quantity': quantity
        }})

        response = jsonify({'mensaje': 'Usuario ' + id + ' fue actualizado satisfactoriamente'})
    
    return response
        
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'mensaje': 'Recurso no encontrado: ' + request.url, 
        'status': 404
    })
    response.status_code = 404

    return response

if __name__ == "__main__":
    app.run(debug=True)