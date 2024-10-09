from .utils.Rol import Rol
from datetime import datetime

class Usuario:
    nombre: str
    apellidos: str
    fecha_nacimiento: datetime
    CURP: str
    
    def __init__(self, us_nombre: str, us_apellido: str, us_fecha_nacimiento: datetime, us_CURP: str):
        self.nombre = us_nombre
        self.apellidos = us_apellido
        self.fecha_nacimiento = us_fecha_nacimiento
        self.CURP = us_CURP
        pass