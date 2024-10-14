from datetime import datetime
from Empleados.CL_Empleado import Empleado
from Guia.CL_Guía import Guia
from Usuarios.CL_Usuario import Usuario
from Veterinario.CL_Veterinario import Veterinario
from Mantenimiento.CL_Mantenimiento import Mantenimiento
from Animales.CL_Animal import Animal
from Visitantes.CL_Visitante import Visitante
from Visita.CL_Visita import Visita
from typing import List

class Zoologico:

    lista_usuarios: List[Usuario] = []
    lista_empleados: List[Empleado] = []

    lista_veterinarios: List[Veterinario] = []
    lista_mantenimiento: List[Mantenimiento] = []
    lista_guias: List[Guia] = []
    lista_animales: List[Animal] = []
    lista_visitantes_adultos: List[Visitante] = []
    lista_visitantes_niños: List[Visitante] = []
    lista_visitas: List[Visita] = []

    def __init__(self):
        visitante_1 = Visitante(
            vi_nombre = "Patty",
            vi_apellido = "Aguado",
            vi_fecha_nacimiento = datetime(2004, 9, 7),
            vi_CURP = "ANAPAT001",
            vi_num_visitas = 4,
            vi_fecha_reg = datetime(2024, 1, 1)
            )
        self.lista_visitantes_adultos.append(visitante_1)
        
        visitante_2 = Visitante(
            vi_nombre = "Carlos",
            vi_apellido = "Rubio",
            vi_fecha_nacimiento = datetime(2010, 7, 7),
            vi_CURP = "JACOBO002",
            vi_num_visitas = 3,
            vi_fecha_reg = datetime(2023, 1, 1)
            )
        self.lista_visitantes_niños.append(visitante_2)

        guia_1 = Guia(
            guia_nombre = "Miguel",
            guia_apellido = "Lemus",
            guia_CURP = "MILEM001",
            guia_fecha_nacimiento = datetime(2003, 8, 28),
            guia_fecha_ingreso = datetime(2020, 1, 1),
            guia_RFC = "LEMUSPAPU",
            guia_salario = 9.99,
            guia_horario = "09 a.m. - 11 p.m."
            )
        self.lista_guias.append(guia_1)
        
        guia_2 = Guia(
            guia_nombre = "Ian",
            guia_apellido = "Cortés",
            guia_CURP = "CORIAN002",
            guia_fecha_nacimiento = datetime(2003, 5, 21),
            guia_fecha_ingreso = datetime(2021, 2, 2),
            guia_RFC = "CORTESPAPU",
            guia_salario = 99.99,
            guia_horario = "09 a.m. - 07 p.m."
            )
        self.lista_guias.append(guia_2)

    def reg_veterinario(self, veterinarioReg: Veterinario):
        self.lista_empleados.append(veterinarioReg)
        self.lista_usuarios.append(veterinarioReg)
        self.lista_veterinarios.append(veterinarioReg)

    def reg_mantenimiento(self, mantenimientoReg: Mantenimiento):
        self.lista_empleados.append(mantenimientoReg)
        self.lista_usuarios.append(mantenimientoReg)
        self.lista_mantenimiento.append(mantenimientoReg)

    def reg_guia(self, guiaReg: Guia):
        self.lista_empleados.append(guiaReg)
        self.lista_usuarios.append(guiaReg)
        self.lista_guias.append(guiaReg)

    def reg_animal(self, animalReg: Animal):
        self.lista_animales.append(animalReg)

    def reg_visitante_mayor(self, visitanteReg: Visitante):
        self.lista_visitantes_adultos.append(visitanteReg)
        self.lista_usuarios.append(visitanteReg)

    def reg_visitante_niños(self, visitanteReg: Visitante):
        self.lista_visitantes_niños.append(visitanteReg)
        self.lista_usuarios.append(visitanteReg)

    def reg_visita(self, guias_CURPS: str, vi_CURPS: list):

        fecha_visita = datetime.now()
        
        guias_encontrados = []

        for guia_CURP in guias_CURPS:

            encontrado = False

            for guia in self.lista_guias:
                if guia.CURP == guia_CURP:
                    guias_encontrados.append(guia)
                    encontrado = True

            if not encontrado:
                print(f"El guia con CURP {guia_CURP} no está registrado.")

        visitantes_encontrados = []
        cant_ninos = 0
        cant_adul = 0

        for vi_CURP in vi_CURPS:

            encontrado = False

            for visitante in self.lista_visitantes_adultos + self.lista_visitantes_niños:
                if visitante.CURP == vi_CURP:
                    visitantes_encontrados.append(visitante)
                    if visitante in self.lista_visitantes_adultos:
                        cant_adul += 1
                        encontrado = True

                    else:
                        cant_ninos += 1
                        encontrado = True
                        break

            if not encontrado:
                print(f"El visitante con CURP {vi_CURP} no está registrado.")

        if len(visitantes_encontrados) > 0:

            nueva_visita = Visita(
                cant_ninos=cant_ninos,
                cant_adul=cant_adul,
                fecha_visita=fecha_visita,
                guia_CURPS=[guia.CURP for guia in guias_encontrados],
                vi_CURPS=[visitante.CURP for visitante in visitantes_encontrados])
        
            self.lista_visitas.append(nueva_visita)
            print(f"Visita registrada exitosamente con {cant_ninos} niños y {cant_adul} adultos.")

        else:
            print("No se puede realizar la visita, no hay visitantes registrados.")
        
    
    def mostrar_veterinarios(self):
        print("\n+++ VETERINARIOS +++\n")
        for veterinario in self.lista_veterinarios:
            print(veterinario.mostrar_info_empleado())
            return
        
    def mostrar_mantenimientos(self):
        print("\n+++ MANTENIMIENTO +++\n")
        for mantenimiento in self.lista_mantenimiento:
            print(mantenimiento.mostrar_info_empleado())
            return
        
    def mostrar_guias(self):
        print("\n+++ GUÍAS +++\n")
        for guia in self.lista_guias:
            print(guia.mostrar_info_empleado())
            return
        
    def mostrar_animales(self):
        print("\n+++ ANIMALES +++\n")
        for animal in self.lista_animales:
            print(animal.mostrar_info_animal())
            return

    def mostrar_visitantes(self):
        print("\n+++ VISITANTES +++\n")
        for visitante in self.lista_visitantes_adultos:
            print("+++ ADULTOS +++")
            print(visitante.mostrar_info_visitante())
            return

        for visitante in self.lista_visitantes_niños:
            print("\n+++ NIÑOS +++\n")
            print(visitante.mostrar_info_visitante())
            return

    def mostrar_visitas(self):
        print("\n+++ VISITAS +++\n")
        for visita in self.lista_visitas:
            print(visita.mostrar_info_visita())
    
    
    
    pass