from Usuarios.CL_Usuario import Usuario
from Usuarios.utils import Rol
from datetime import datetime

class Visitante(Usuario):
    vi_num_visitas: int
    vi_fecha_reg: datetime
    
    def __init__(self) -> None:
        pass
    pass