from Usuarios.CL_Usuario import Usuario
from Usuarios.utils.Rol import Roles
from datetime import datetime

class CL_Director(Usuario):
    def __init__(self, dir_nombre: str,
                 dir_apellido: str,
                 dir_CURP: str,
                 dir_fecha_nacimiento: datetime
                 ):
        
        super().__init__(
            us_nombre=dir_nombre,
            us_apellido=dir_apellido,
            us_CURP=dir_CURP,
            us_fecha_nacimiento=dir_fecha_nacimiento,
            rol=Roles.DIRECTOR)
