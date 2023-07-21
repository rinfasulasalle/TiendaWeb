from backend.models.mysql_connection_pool import MySQLPool

class ProductosModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_producto(self, id_producto):
        params = {'id_producto': id_producto}
        rv = self.mysql_pool.execute("SELECT * FROM Productos WHERE id_producto = %(id_producto)s", params)
        data = []
        for result in rv:
            content = {
                'id_producto': result[0],
                'nombre': result[1],
                'precio': float(result[2]),
                'talla': result[3],
                'categoria_id': result[4],
                'imagen_url': result[5],
                'stock': result[6]
            }
            data.append(content)
        return data

    def get_productos(self):
        rv = self.mysql_pool.execute("SELECT * FROM Productos")
        data = []
        for result in rv:
            content = {
                'id_producto': result[0],
                'nombre': result[1],
                'precio': float(result[2]),
                'talla': result[3],
                'categoria_id': result[4],
                'imagen_url': result[5],
                'stock': result[6]
            }
            data.append(content)
        return data

    def create_producto(self, nombre, precio, talla, categoria_id, imagen_url, stock):
        # Verificar si la categoria_id existe en la tabla Categorias antes de crear el producto
        if not self.categoria_exists(categoria_id):
            raise ValueError("La categoria_id especificada no existe en la tabla Categorias.")
        
        data = {
            'nombre': nombre,
            'precio': float(precio),
            'talla': talla,
            'categoria_id': categoria_id,
            'imagen_url': imagen_url,
            'stock': stock
        }
        query = """INSERT INTO Productos (nombre, precio, talla, categoria_id, imagen_url, stock)
                   VALUES (%(nombre)s, %(precio)s, %(talla)s, %(categoria_id)s, %(imagen_url)s, %(stock)s)"""
        cursor = self.mysql_pool.execute(query, data, commit=True)
        data['id_producto'] = cursor.lastrowid
        return data

    def update_producto(self, id_producto, nombre, precio, talla, categoria_id, imagen_url, stock):
        # Verificar si el id_producto existe antes de realizar la actualización
        if not self.producto_exists(id_producto):
            raise ValueError("El id_producto especificado no existe en la tabla Productos.")
        
        # Verificar si la categoria_id existe en la tabla Categorias antes de realizar la actualización
        if not self.categoria_exists(categoria_id):
            raise ValueError("La categoria_id especificada no existe en la tabla Categorias.")
        
        data = {
            'id_producto': id_producto,
            'nombre': nombre,
            'precio': float(precio),
            'talla': talla,
            'categoria_id': categoria_id,
            'imagen_url': imagen_url,
            'stock': stock
        }
        query = """UPDATE Productos SET nombre = %(nombre)s, precio = %(precio)s, talla = %(talla)s,
                   categoria_id = %(categoria_id)s, imagen_url = %(imagen_url)s, stock = %(stock)s
                   WHERE id_producto = %(id_producto)s"""
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_producto(self, id_producto):
        # Verificar si el id_producto existe antes de realizar la eliminación
        if not self.producto_exists(id_producto):
            raise ValueError("El id_producto especificado no existe en la tabla Productos.")
        
        params = {'id_producto': id_producto}
        query = "DELETE FROM Productos WHERE id_producto = %(id_producto)s"
        self.mysql_pool.execute(query, params, commit=True)
        result = {'result': 1}
        return result

    def producto_exists(self, id_producto):
        params = {'id_producto': id_producto}
        rv = self.mysql_pool.execute("SELECT id_producto FROM Productos WHERE id_producto = %(id_producto)s", params)
        return bool(rv)

    def categoria_exists(self, categoria_id):
        params = {'categoria_id': categoria_id}
        rv = self.mysql_pool.execute("SELECT id_categoria FROM Categorias WHERE id_categoria = %(categoria_id)s", params)
        return bool(rv)
