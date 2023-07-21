from backend.models.mysql_connection_pool import MySQLPool

class TipoUsuarioModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_tipo_usuario(self, tipo_usuario_id):
        params = {'tipo_usuario_id': tipo_usuario_id}
        rv = self.mysql_pool.execute("SELECT * FROM TipoUsuario WHERE id_tipoUsuario = %(tipo_usuario_id)s", params)
        data = []
        for result in rv:
            content = {'tipo_usuario_id': result[0], 'nombre': result[1]}
            data.append(content)
        return data

    def get_tipos_usuarios(self):
        rv = self.mysql_pool.execute("SELECT * FROM TipoUsuario")
        data = []
        for result in rv:
            content = {'tipo_usuario_id': result[0], 'nombre': result[1]}
            data.append(content)
        return data

    def create_tipo_usuario(self, nombre):
        data = {'nombre': nombre}
        query = "INSERT INTO TipoUsuario (nombre) VALUES (%(nombre)s)"
        cursor = self.mysql_pool.execute(query, data, commit=True)
        data['tipo_usuario_id'] = cursor.lastrowid
        return data

    def update_tipo_usuario(self, tipo_usuario_id, nombre):
        data = {'tipo_usuario_id': tipo_usuario_id, 'nombre': nombre}
        query = "UPDATE TipoUsuario SET nombre = %(nombre)s WHERE id_tipoUsuario = %(tipo_usuario_id)s"
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_tipo_usuario(self, tipo_usuario_id):
        params = {'tipo_usuario_id': tipo_usuario_id}
        query = "DELETE FROM TipoUsuario WHERE id_tipoUsuario = %(tipo_usuario_id)s"
        self.mysql_pool.execute(query, params, commit=True)
        result = {'result': 1}
        return result
