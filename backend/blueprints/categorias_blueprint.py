from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from backend.models.mysql_categorias_model import CategoriasModel

categorias_model = CategoriasModel()

categorias_blueprint = Blueprint('categorias_blueprint', __name__)

@categorias_blueprint.route('/categoria', methods=['PUT'])
@cross_origin()
def create_categoria():
    content = categorias_model.create_categoria(request.json['nombre'])
    return jsonify(content)

@categorias_blueprint.route('/categoria', methods=['PATCH'])
@cross_origin()
def update_categoria():
    content = categorias_model.update_categoria(request.json['id_categoria'], request.json['nombre'])
    return jsonify(content)

@categorias_blueprint.route('/categoria', methods=['DELETE'])
@cross_origin()
def delete_categoria():
    return jsonify(categorias_model.delete_categoria(int(request.json['id_categoria'])))

@categorias_blueprint.route('/categoria', methods=['POST'])
@cross_origin()
def get_categoria():
    return jsonify(categorias_model.get_categoria(int(request.json['id_categoria'])))

@categorias_blueprint.route('/categorias', methods=['POST'])
@cross_origin()
def get_categorias():
    return jsonify(categorias_model.get_categorias())
