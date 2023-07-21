from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from backend.models.mysql_productos_model import ProductosModel

producto_model = ProductosModel()

producto_blueprint = Blueprint('producto_blueprint', __name__)

@producto_blueprint.route('/producto', methods=['PUT'])
@cross_origin()
def create_producto():
    content = producto_model.create_producto(
        request.json['nombre'],
        request.json['precio'],
        request.json['talla'],
        request.json['categoria_id'],
        request.json['imagen_url'],
        request.json['stock']
    )
    return jsonify(content)

@producto_blueprint.route('/producto', methods=['PATCH'])
@cross_origin()
def update_producto():
    content = producto_model.update_producto(
        request.json['id_producto'],
        request.json['nombre'],
        request.json['precio'],
        request.json['talla'],
        request.json['categoria_id'],
        request.json['imagen_url'],
        request.json['stock']
    )
    return jsonify(content)

@producto_blueprint.route('/producto', methods=['DELETE'])
@cross_origin()
def delete_producto():
    return jsonify(producto_model.delete_producto(int(request.json['id_producto'])))

@producto_blueprint.route('/producto', methods=['POST'])
@cross_origin()
def get_producto():
    return jsonify(producto_model.get_producto(int(request.json['id_producto'])))

@producto_blueprint.route('/productos', methods=['POST'])
@cross_origin()
def get_productos():
    return jsonify(producto_model.get_productos())
