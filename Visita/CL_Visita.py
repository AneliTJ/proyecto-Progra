from typing import List
from Guia.CL_Guía import Guia
from Visitantes.CL_Visitante import Visitante
from datetime import datetime

class Visita:
    no_guias_visita: 0
    no_visitantes_visita: 0
    costo_total: float
    cant_ninos: int
    cant_adul: int
    fecha_visita: datetime


    def __init__(self, costo_total: float, cant_ninos: int, cant_adul:int, fecha_visita: datetime):
        self.costo_total = costo_total
        self.cant_ninos = cant_ninos
        self.cant_adultos = cant_adul
        self.fecha_visita = fecha_visita
        self.guias: List[Guia] = []
        self.visitantes: List[Visitante] = []
        self.no_guias_visita = 0
        self.no_visitantes_visita = 0 

        pass

    def registrar_guia(self, guia: Guia):
        self.no_guias_visita += 1
        self.guias.append(guia)

    def registrar_visitante(self, visitante: Visitante):
        self.no_visitantes_visita += 1
        self.visitantes.append(visitante)

    def mostrar_info_visita(self):
        info = f"Fecha de visita: {self.fecha_visita}\n"
        info += f"Costo total: {self.costo_total}\n"
        info += f"Cantidad de niños: {self.cant_ninos}, Adultos: {self.cant_adultos}\n"
        info += "Guías:\n"
        
        if self.guias:
            for guia in self.guias:
                info += f"  - {guia.mostrar_info_empleado()}\n"
        else:
            info += "  No hay guías asignados a esta visita.\n"
        
        info += "Visitantes:\n"
        
        if self.visitantes:
            for visitante in self.visitantes:
                info += f"  - {visitante.mostrar_info_visitante()}\n"
        else:
            info += "  No hay visitantes asignados a esta visita.\n"

        return info