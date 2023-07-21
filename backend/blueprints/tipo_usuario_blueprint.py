from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from backend.models.mysql_tipo_usuario_model import TipoUsuarioModel

tipo_usuario_model = TipoUsuarioModel()

tipo_usuario_blueprint = Blueprint('tipo_usuario_blueprint', __name__)

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['PUT'])
@cross_origin()
def create_tipo_usuario():
    content = tipo_usuario_model.create_tipo_usuario(request.json['nombre'])
    return jsonify(content)

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['PATCH'])
@cross_origin()
def update_tipo_usuario():
    content = tipo_usuario_model.update_tipo_usuario(request.json['tipo_usuario_id'], request.json['nombre'])
    return jsonify(content)

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['DELETE'])
@cross_origin()
def delete_tipo_usuario():
    return jsonify(tipo_usuario_model.delete_tipo_usuario(int(request.json['tipo_usuario_id'])))

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['POST'])
@cross_origin()
def get_tipo_usuario():
    return jsonify(tipo_usuario_model.get_tipo_usuario(int(request.json['tipo_usuario_id'])))

@tipo_usuario_blueprint.route('/tipo_usuarios', methods=['POST'])
@cross_origin()
def get_tipos_usuarios():
    return jsonify(tipo_usuario_model.get_tipos_usuarios())
