-- Create the database
CREATE DATABASE nucleo_diagnostico;

-- Connect to the newly created database
\c nucleo_diagnostico;

-- Create the 'pacientes' table
CREATE TABLE pacientes (
    codigo SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    fecha_nac DATE,
    sexo VARCHAR(10),
    edad INTEGER,
    estatura NUMERIC(5, 2)
);

-- Create the 'empleado' table
CREATE TABLE empleado (
    codigo SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    fecha_nac DATE,
    sexo VARCHAR(1),
    sueldo NUMERIC(10, 2),
    turno VARCHAR(50),
    contrasena VARCHAR(255)
);

-- Create the 'doctores' table
CREATE TABLE doctores (
    codigo SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    fecha_nac DATE,
    sexo VARCHAR(10),
    especialidad VARCHAR(100),
    contrasena VARCHAR(255)
);
