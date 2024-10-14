from datetime import datetime
from Veterinario.CL_Veterinario import Veterinario
from Zoologico.CL_Zoologico import Zoologico
from Guia.CL_Guía import Guia
from Mantenimiento.CL_Mantenimiento import Mantenimiento
from Animales.CL_Animal import Animal
from Visitantes.CL_Visitante import Visitante
from Visita.CL_Visita import Visita


class Menú:
    zoo: Zoologico = Zoologico()
    
    
    def mostrar_menú(self):
        num_visitas =0
        precio = 0
        while True:
            print(
                """
    ++++++ ZOOLÓGICO ++++++

    1. Registrar Empleado (Veterinario)
    2. Registrar Empleado (Mantenimiento)
    3. Registrar Empleado (Guía)
    4. Registrar Animal
    5. Registrar Visitante
    6. Registrar Visita

    10. Mostrar Empleados (Veterinario)
    11. Mostrar Empleados (Mantenimiento)
    12. Mostrar Empleados (Guía)
    13. Mostrar Animales
    14. Mostrar Visitantes
    15. Mostrar Visitas
    
    20.Costo de la visita


    40. Salir
    """
            )

            opcion = int(input("\nIngresa la función a realizar: "))

            if opcion == 1:
                print("\n+++ Registrar Empleado (Veterinario) +++")
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa los apellidos: ")
                curp =  input("Ingresa la CURP: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento: "))
                f_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

                dia_ingreso = int(input("Ingresa el día de ingreso: "))
                mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                año_ingreso = int(input("Ingresa el año de ingreso: "))
                f_ingreso = datetime(año_ingreso, mes_ingreso, dia_ingreso)
                rfc = input("Ingresa el RFC: ")
                salario = input("Ingresa el salario: ")
                horario = input("Ingresa el horario: ")

                _veterinario = Veterinario(vet_nombre=nombre,
                                        vet_apellido=apellido,
                                        vet_CURP=curp,
                                        vet_fecha_nacimiento=f_nacimiento,
                                        vet_fecha_ingreso=f_ingreso,
                                        vet_RFC=rfc,
                                        vet_salario=salario,
                                        vet_horario=horario)
                
                self.zoo.reg_veterinario(_veterinario)
                self.zoo.reg_veterinario(veterinarioReg=_veterinario)

            if opcion == 2:
                print("\n+++ Registrar Empleado (Mantenimineto) +++")
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa los apellidos: ")
                curp =  input("Ingresa la CURP: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento: "))
                f_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

                dia_ingreso = int(input("Ingresa el día de ingreso: "))
                mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                año_ingreso = int(input("Ingresa el año de ingreso: "))
                f_ingreso = datetime(año_ingreso, mes_ingreso, dia_ingreso)

                rfc = input("Ingresa el RFC: ")
                salario = input("Ingresa el salario: ")
                horario = input("Ingresa el horario: ")

                _mantenimiento = Mantenimiento(mant_nombre=nombre,
                                        mant_apellido=apellido,
                                        mant_CURP=curp,
                                        mant_fecha_nacimiento=f_nacimiento,
                                        mant_fecha_ingreso=f_ingreso,
                                        mant_RFC=rfc,
                                        mant_salario=salario,
                                        mant_horario=horario)
                
                self.zoo.reg_mantenimiento(_mantenimiento)
                self.zoo.reg_mantenimiento(mantenimientoReg=_mantenimiento)

            if opcion == 3:
                print("\n+++ Registrar Empleado (Guía) +++")
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa los apellidos: ")
                curp =  input("Ingresa la CURP: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento: "))
                f_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

                dia_ingreso = int(input("Ingresa el día de ingreso: "))
                mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                año_ingreso = int(input("Ingresa el año de ingreso: "))
                f_ingreso = datetime(año_ingreso, mes_ingreso, dia_ingreso)

                rfc = input("Ingresa el RFC: ")
                salario = input("Ingresa el salario: ")
                horario = input("Ingresa el horario: ")

                _guia = Guia(guia_nombre=nombre,
                             guia_apellido=apellido,
                             guia_CURP=curp,
                             guia_fecha_nacimiento=f_nacimiento,
                             guia_fecha_ingreso=f_ingreso,
                             guia_RFC=rfc,
                             guia_salario=salario,
                             guia_horario=horario)
                
                self.zoo.reg_guia(_guia)
                self.zoo.reg_guia(guiaReg=_guia)

            if opcion == 4:
                print("\n+++ Registrar Animal +++")
                id_animal = input("Ingresa el ID del animal: ")
                tipo_animal = input("Ingresa el tipo de animal: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento: "))
                f_ani_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

                dia_llegada = int(input("Ingresa el día de llegada: "))
                mes_llegada = int(input("Ingresa el mes de llegada: "))
                año_llegada = int(input("Ingresa el año de llegada: "))
                f_llegada = datetime(año_llegada, mes_llegada, dia_llegada)

                enfermedades = []
                while True:
                     enfermedad = input("Ingresa las enfermedades o fin en caso de no contar con ninguna: ")
                     if enfermedad.lower() in ["fin", "f", "nif", "fni"]:
                         break
                     enfermedades.append(enfermedad)

                tipo_alimentacion = input("Ingresa el tipo de alimentación: ")
                peso = input("Ingresa el peso del animal: ")
                frec_alimentación = input("Ingresa la frecuencia de alimentación: ")
                vacunas = input("¿Cuenta con vacunas? (s/n): ").lower() == 's'

                _animal = Animal(
                    id_animal=id_animal,
                    tipo_animal=tipo_animal,
                    fecha_llegada=f_llegada,
                    fecha_nacimiento=f_ani_nacimiento,
                    enfermedades=enfermedades,
                    tipo_alimentacion=tipo_alimentacion,
                    peso=peso,
                    frecuencia_alimentacion=frec_alimentación,
                    vacunas=vacunas
                )

                self.zoo.reg_animal(_animal)
                self.zoo.reg_animal(animalReg=_animal)

            if opcion == 5:
                print("\n+++ Registrar Visitante +++")
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa los apellidos: ")
                curp =  input("Ingresa la CURP: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento_vis = int(input("Ingresa el año de nacimiento: "))
                f_nacimiento = datetime(año_nacimiento_vis, mes_nacimiento, dia_nacimiento)
                dia_ingreso = int(input("Ingresa el día de ingreso: "))
                mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                año_ingreso = int(input("Ingresa el año de ingreso: "))
                f_ingreso = datetime(año_ingreso, mes_ingreso, dia_ingreso)

                _visitante = Visitante(
                    vi_nombre=nombre,
                    vi_apellido=apellido,
                    vi_CURP=curp,
                    vi_fecha_nacimiento=f_nacimiento,
                    vi_fecha_reg=f_ingreso,
                    vi_num_visitas=num_visitas)
                
                if (datetime.now().year) - (año_nacimiento_vis) >= 18:
                    self.zoo.reg_visitante_mayor(_visitante)
                    self.zoo.reg_visitante_mayor(visitanteReg=_visitante)

                else:
                    self.zoo.reg_visitante_niños(_visitante)
                    self.zoo.reg_visitante_niños(visitanteReg=_visitante)
                
            if opcion == 6:
                print("\n+++ Registrar Visita +++")
                cant_ninos = int(input("Ingrese la cantidad de niños: "))
                cant_adul = int(input("Ingrese la cantidad de adultos: "))
                fecha = datetime.now()
                guia_CURP = input("Ingresa el CURP del guía: ")
                vi_CURPS = input("Ingresa las CURP de los visitantes (separadas por comas): ").split(',')
                vi_CURPS = [vi_CURP.strip() for vi_CURP in vi_CURPS]

                _visita = Visita(
                                 cant_ninos=cant_ninos,
                                 cant_adul=cant_adul,
                                 fecha_visita=fecha,
                                 guia_CURP=guia_CURP,
                                 vi_CURPS=vi_CURPS)
                                
                self.zoo.reg_visita(_visita)
         
            if opcion == 10:
                self.zoo.mostrar_veterinarios()
                pass

            if opcion == 11:
                self.zoo.mostrar_mantenimientos()
                pass

            if opcion == 12:
                self.zoo.mostrar_guias()
                pass
            
            if opcion == 13:
                self.zoo.mostrar_animales()
                pass

            if opcion == 14:
                self.zoo.mostrar_visitantes()
                pass

            if opcion == 15:
                self.zoo.mostrar_visitas()

            if opcion == 20:
                print("\n+++ Costo de la visita +++")
                print(precio)

            if opcion == 40:
                precio = 0
                break
