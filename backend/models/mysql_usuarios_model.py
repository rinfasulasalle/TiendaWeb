from backend.models.mysql_connection_pool import MySQLPool

class UsuariosModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_usuario(self, usuario_id):
        params = {'usuario_id': usuario_id}
        rv = self.mysql_pool.execute("SELECT * FROM Usuarios WHERE id_usuario = %(usuario_id)s", params)
        data = []
        for result in rv:
            content = {
                'id_usuario': result[0],
                'tipo_usuario_id': result[1],
                'nombre': result[2],
                'direccion': result[3],
                'telefono': result[4],
                'email': result[5]
            }
            data.append(content)
        return data

    def get_usuarios(self):
        rv = self.mysql_pool.execute("SELECT * FROM Usuarios")
        data = []
        for result in rv:
            content = {
                'id_usuario': result[0],
                'tipo_usuario_id': result[1],
                'nombre': result[2],
                'direccion': result[3],
                'telefono': result[4],
                'email': result[5]
            }
            data.append(content)
        return data

    def create_usuario(self, tipo_usuario_id, nombre, direccion=None, telefono=None, email=None):
        # Verificar si el tipo de usuario existe antes de crear el usuario
        tipo_usuario = self.get_tipo_usuario(tipo_usuario_id)
        if not tipo_usuario:
            return {'error': 'Tipo de usuario no encontrado'}

        data = {
            'tipo_usuario_id': tipo_usuario_id,
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'email': email
        }
        query = "INSERT INTO Usuarios (tipo_usuario_id, nombre, direccion, telefono, email) VALUES (%(tipo_usuario_id)s, %(nombre)s, %(direccion)s, %(telefono)s, %(email)s)"
        cursor = self.mysql_pool.execute(query, data, commit=True)
        data['id_usuario'] = cursor.lastrowid
        return data

    def update_usuario(self, usuario_id, tipo_usuario_id, nombre, direccion=None, telefono=None, email=None):
        # Verificar si el tipo de usuario existe antes de actualizar el usuario
        tipo_usuario = self.get_tipo_usuario(tipo_usuario_id)
        if not tipo_usuario:
            return {'error': 'Tipo de usuario no encontrado'}

        data = {
            'usuario_id': usuario_id,
            'tipo_usuario_id': tipo_usuario_id,
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'email': email
        }
        query = "UPDATE Usuarios SET tipo_usuario_id = %(tipo_usuario_id)s, nombre = %(nombre)s, direccion = %(direccion)s, telefono = %(telefono)s, email = %(email)s WHERE id_usuario = %(usuario_id)s"
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_usuario(self, usuario_id):
        params = {'usuario_id': usuario_id}
        query = "DELETE FROM Usuarios WHERE id_usuario = %(usuario_id)s"
        self.mysql_pool.execute(query, params, commit=True)
        result = {'result': 1}
        return result

    def get_tipo_usuario(self, tipo_usuario_id):
        params = {'tipo_usuario_id': tipo_usuario_id}
        rv = self.mysql_pool.execute("SELECT * FROM TipoUsuario WHERE id_tipoUsuario = %(tipo_usuario_id)s", params)
        return rv
