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
from random import randint

class Zoologico:

    lista_usuarios: List[Usuario] = []
    lista_empleados: List[Empleado] = []

    lista_veterinarios: List[Veterinario] = []
    lista_mantenimiento: List[Mantenimiento] = []
    lista_guias: List[Guia] = []
    lista_animales: List[Animal] = []
    lista_visitantes: List[Visitante] = []
    lista_visitas: List[Visita] = []

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

    def reg_visitante(self, visitanteReg: Visitante):
        self.lista_visitantes.append(visitanteReg)
        self.lista_usuarios.append(visitanteReg)

    def reg_visita(self, visitaReg: Visita):
        guia = None
        visitantes_encontrados = []
        
        for guia_reg in self.lista_guias:
            if guia_reg.CURP == visitaReg.guia_CURP:
                guia = guia_reg
                break
        
        if not guia:
            print(f"El guía con CURP {visitaReg.guia_CURP} no está registrado.")
            return

        for vi_CURP in visitaReg.vi_CURPS:
            encontrado = False
            for visitante in self.lista_visitantes:
                if visitante.CURP == vi_CURP:
                    visitantes_encontrados.append(visitante)
                    encontrado = True
                    break
            if not encontrado:
                print(f"El visitante con CURP {vi_CURP} no está registrado.")

        if len(visitantes_encontrados) > 0:
            nueva_visita = Visita(
                costo_total=visitaReg.costo_total,
                cant_ninos=visitaReg.cant_ninos,
                cant_adul=visitaReg.cant_adul,
                fecha_visita=visitaReg.fecha_visita,
                guia_CURP=guia.CURP,  # Aquí pasas el CURP del guía
                vi_CURPS=[visitante.CURP for visitante in visitantes_encontrados]  # Lista de CURP de los visitantes
            )
            
            self.lista_visitas.append(nueva_visita)
            print("Visita registrada exitosamente.")
        else:
            print("No se puede realizar la visita, no hay visitantes registrados.")
    
    def mostrar_veterinarios(self):
        print("`\n+++ VETERINARIOS +++\n")
        for veterinario in self.lista_veterinarios:
            print(veterinario.mostrar_info_empleado())
            return
        
    def mostrar_mantenimientos(self):
        print("`\n+++ MANTENIMIENTO +++\n")
        for mantenimiento in self.lista_mantenimiento:
            print(mantenimiento.mostrar_info_empleado())
            return
        
    def mostrar_guias(self):
        print("`\n+++ GUÍAS +++\n")
        for guia in self.lista_guias:
            print(guia.mostrar_info_empleado())
            return
        
    def mostrar_animales(self):
        print("`\n+++ ANIMALES +++\n")
        for animal in self.lista_animales:
            print(animal.mostrar_info_animal())
            return

    def mostrar_visitantes(self):
        print("`\n+++ VISITANTES +++\n")
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())
        
    def mostrar_visitas(self):
        print("`\n+++ VISITAS +++\n")
        for visita in self.lista_visitas:
            print(visita.mostrar_info_visita())

    def generar_id_visitantes(self):
        num_rand= randint (1,10000)
        nu_visi= len(self.lista_visitantes)+1
        id_visita=f"{num_rand}{nu_visi}"
        return id_visita

    
    
    
    
    pass