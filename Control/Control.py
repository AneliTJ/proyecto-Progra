from typing import List
from Animales import CL_Animal
from Empleados import CL_Empleado
from datetime import datetime

class Control: 
    mant_CURP: str
    proceso: str
    observaciones: str
    fecha_proceso: datetime 
    id_animal: str

    def __init__(self, mant_CURP: str, proceso: str, observaciones: str, fecha_proceso: datetime, id_animal: str):
        self.mant_CURP= mant_CURP
        self.proceso = proceso
        self.observaciones = observaciones
        self.fecha_proceso = fecha_proceso
