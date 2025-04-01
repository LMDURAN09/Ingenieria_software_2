CREATE DATABASE ChatErrores;
USE ChatErrores;
-- Crear la tabla Administrador
CREATE TABLE Administrador (
    ID_Usuario INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL
);

-- Crear la tabla Aplicacion
CREATE TABLE Aplicacion (
    ID_aplicacion INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT,
    ID_Administrador INT,
    CONSTRAINT FK_ID_Administrador FOREIGN KEY (ID_Administrador) REFERENCES Administrador(ID_Usuario)
);

-- Crear la tabla Error
CREATE TABLE Error (
    ID_error INT PRIMARY KEY,
    ID_aplicacion INT,
    Codigo_error VARCHAR(50) NOT NULL,
    Descripcion TEXT,
    Solucion TEXT,
    CONSTRAINT FK_ID_Aplicacion FOREIGN KEY (ID_aplicacion) REFERENCES Aplicacion(ID_aplicacion)
);

-- Crear la tabla Usuario
CREATE TABLE Usuario (
    ID_Usuario INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Correo VARCHAR(100) NOT NULL UNIQUE,
    Rol VARCHAR(50) NOT NULL
);

-- Crear la tabla Hist_consulta
CREATE TABLE Hist_consulta (
    ID_consulta INT PRIMARY KEY,
    ID_usuario INT,
    ID_error INT,
    Fecha DATETIME NOT NULL,
    CONSTRAINT FK_ID_Usuario FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_Usuario),
    CONSTRAINT FK_ID_Error FOREIGN KEY (ID_error) REFERENCES Error(ID_error)
);




Drop database ChatErrores;
