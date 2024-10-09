from Usuarios.CL_Usuario import Usuario
from datetime import datetime


class CL_Empleado(Usuario):
    fecha_ingreso_em: datetime
    rfc: str
    salario: float
    horario: str

    def __init__(self, em_nombre: str, em_apellido: str, em_fecha_nacimiento: datetime,em_fecha_ingreso:datetime, em_rfc:str, em_salario:float, em_horario:str, us_CURP: str):
        super().__init__(
            em_nombre, 
            em_apellido, 
            em_fecha_nacimiento, 
            em_CURP)
        self.fecha_ingreso_em
        self.rfc
        self.salario
        self.horario