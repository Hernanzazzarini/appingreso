-- Tabla personal
CREATE TABLE personal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_persona VARCHAR(255),
    telefono VARCHAR(15),
    dni VARCHAR(20)
);

-- Tabla sector
CREATE TABLE sector (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_sector VARCHAR(255)
);

-- Tabla ingreso
CREATE TABLE ingreso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT,
    id_sector INT,
    horario_ingreso DATETIME,
    horario_salida DATETIME,
    horas_trabajadas_diarias DECIMAL(5, 2) DEFAULT 0,
    FOREIGN KEY (id_persona) REFERENCES personal(id),
    FOREIGN KEY (id_sector) REFERENCES sector(id)
);