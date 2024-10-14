from typing import List
from Guia.CL_Guía import Guia
from Visitantes.CL_Visitante import Visitante
from datetime import datetime

class Visita:
    # costo_total: float
    cant_ninos: int
    cant_adul: int
    fecha_visita: datetime
    guia_CURP: str
    visitantes: List[Visitante] = []

    def __init__(self, cant_ninos: int, cant_adul: int, fecha_visita: datetime, guia_CURP: str, vi_CURPS: List[str]):
        # self.costo_total = costo_total
        self.cant_ninos = cant_ninos
        self.cant_adul = cant_adul
        self.fecha_visita = fecha_visita
        self.guia_CURP = guia_CURP
        self.vi_CURPS = vi_CURPS 

    def mostrar_info_visita(self):
        return f"""
        Cantidad de niños: {self.cant_ninos}
        Cantidad de adultos: {self.cant_adul}
        Fecha de la visita: {self.fecha_visita}
        Guía: {self.guia_CURP}
        Visitantes: {', '.join(self.vi_CURPS)}
        """
