from backend.models.mysql_connection_pool import MySQLPool

class CategoriasModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_categoria(self, categoria_id):
        params = {'categoria_id': categoria_id}
        rv = self.mysql_pool.execute("SELECT * FROM Categorias WHERE id_categoria = %(categoria_id)s", params)
        data = []
        for result in rv:
            content = {'id_categoria': result[0], 'nombre': result[1]}
            data.append(content)
        return data

    def get_categorias(self):
        rv = self.mysql_pool.execute("SELECT * FROM Categorias")
        data = []
        for result in rv:
            content = {'id_categoria': result[0], 'nombre': result[1]}
            data.append(content)
        return data

    def create_categoria(self, nombre):
        data = {'nombre': nombre}
        query = "INSERT INTO Categorias (nombre) VALUES (%(nombre)s)"
        cursor = self.mysql_pool.execute(query, data, commit=True)
        data['id_categoria'] = cursor.lastrowid
        return data

    def update_categoria(self, categoria_id, nombre):
        if not self._categoria_exists(categoria_id):
            return {'error': f'Categoría con id {categoria_id} no existe.'}

        data = {'categoria_id': categoria_id, 'nombre': nombre}
        query = "UPDATE Categorias SET nombre = %(nombre)s WHERE id_categoria = %(categoria_id)s"
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_categoria(self, categoria_id):
        if not self._categoria_exists(categoria_id):
            return {'error': f'Categoría con id {categoria_id} no existe.'}

        params = {'categoria_id': categoria_id}
        query = "DELETE FROM Categorias WHERE id_categoria = %(categoria_id)s"
        self.mysql_pool.execute(query, params, commit=True)
        result = {'result': 1}
        return result

    def _categoria_exists(self, categoria_id):
        params = {'categoria_id': categoria_id}
        rv = self.mysql_pool.execute("SELECT * FROM Categorias WHERE id_categoria = %(categoria_id)s", params)
        return bool(rv)

