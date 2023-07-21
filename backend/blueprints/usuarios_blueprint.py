from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from backend.models.mysql_usuarios_model import UsuariosModel

usuarios_model = UsuariosModel()

usuarios_blueprint = Blueprint('usuarios_blueprint', __name__)

@usuarios_blueprint.route('/usuario', methods=['PUT'])
@cross_origin()
def create_usuario():
    tipo_usuario_id = request.json['tipo_usuario_id']
    nombre = request.json['nombre']
    direccion = request.json.get('direccion')
    telefono = request.json.get('telefono')
    email = request.json.get('email')

    content = usuarios_model.create_usuario(tipo_usuario_id, nombre, direccion, telefono, email)
    return jsonify(content)

@usuarios_blueprint.route('/usuario', methods=['PATCH'])
@cross_origin()
def update_usuario():
    usuario_id = request.json['id_usuario']
    tipo_usuario_id = request.json['tipo_usuario_id']
    nombre = request.json['nombre']
    direccion = request.json.get('direccion')
    telefono = request.json.get('telefono')
    email = request.json.get('email')

    content = usuarios_model.update_usuario(usuario_id, tipo_usuario_id, nombre, direccion, telefono, email)
    return jsonify(content)

@usuarios_blueprint.route('/usuario', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    usuario_id = request.json['id_usuario']
    return jsonify(usuarios_model.delete_usuario(usuario_id))

@usuarios_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def get_usuario():
    usuario_id = request.json['id_usuario']
    return jsonify(usuarios_model.get_usuario(usuario_id))

@usuarios_blueprint.route('/usuarios', methods=['POST'])
@cross_origin()
def get_usuarios():
    return jsonify(usuarios_model.get_usuarios())
