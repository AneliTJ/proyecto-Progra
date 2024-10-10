from datetime import datetime

class Animal:
    id_animal: str
    tipo_animal:str
    fecha_llegada: datetime
    enfermedades: str
    tipo_alimentacion: str
    fecha_nacimiento: datetime
    peso: str
    frecuencia_alimentacion: str
    vacunas: bool

    def __init__(self, id_animal: str, tipo_animal: str, fecha_llegada: datetime, enfermedades: str, tipo_alimentacion: str, fecha_nacimiento:str, peso:str, frecuencia_alimentacion:str,vacunas:bool):
        self.id_animal = id_animal
        self.tipo_animal = tipo_animal
        self.fecha_llegada = fecha_llegada
        self.enfermedades = enfermedades
        self.tipo_alimentacion = tipo_alimentacion
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.vacunas = vacunas

    def mostrar_info_animal(self):
        info_animal = f"Tipo de animal: {self.tipo_animal},
        Fecha de llegada: {self.fecha_llegada},
        Enfermedades: {self.enfermedades},
        Tipo de alimentacion: {self.tipo_alimentacion},
        Fecha de nacimiento: {self.fecha_nacimiento},
        Peso: {self.peso},
        Frecuencia de alimentacion: {self.frecuencia_alimentacion},
        Vacunas: {self.vacunas}"
        return info_animal