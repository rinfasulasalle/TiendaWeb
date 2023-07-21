-- Tabla "Categorias"
CREATE TABLE Categorias (
	id_categoria INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100) NOT NULL,
);

-- Tabla "Productos"
CREATE TABLE Productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    talla VARCHAR(10) NOT NULL,
    categoria_id INT NOT NULL,
    imagen_url VARCHAR(255),
    stock INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id_categoria)
);

-- Tabla "TipoUsuario"
CREATE TABLE TipoUsuario(
	id_tipoUsuario INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100) NOT NULL,
);

-- Tabla "Usuarios"
CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    tipo_usuario_id INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    FOREIGN KEY (tipo_usuario_id) REFERENCES TipoUsuario(id_tipoUsuario)
);

-- Tabla "Ventas"
CREATE TABLE Ventas (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    id_usuario INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla "DetalleVenta"
CREATE TABLE DetalleVenta (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);
