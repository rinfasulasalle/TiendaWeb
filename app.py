from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.tipo_usuario_blueprint import tipo_usuario_blueprint
from backend.blueprints.usuarios_blueprint import usuarios_blueprint
from backend.blueprints.categorias_blueprint import categorias_blueprint
from backend.blueprints.productos_blueprint import producto_blueprint


app = Flask(__name__)

# Registra el blueprint para la tabla "TipoUsuario"
app.register_blueprint(tipo_usuario_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(categorias_blueprint)
app.register_blueprint(producto_blueprint)
cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
