from datetime import datetime
from Veterinario.CL_Veterinario import Veterinario
from Zoologico.CL_Zoologico import Zoologico
from Guia.CL_Guía import Guia
from Mantenimiento.CL_Mantenimiento import Mantenimiento

class Menú:

    zoo: Zoologico = Zoologico()
    
    def mostrar_menú(self):
        while True:
            print(
                """
    ++++++ ZOOLÓGICO ++++++

    1. Registrar Empleado (Veterinario)
    2. Registrar Empleado (Mantenimiento)
    3. Registrar Empleado (Guía)

    10. Mostrar Empleados (Veterinario)

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
                
                self.zoo.reg_guia(-_guia)
                self.zoo.reg_guia(guiaReg=_guia)

            if opcion == 10:
                self.zoo.mostrar_veterinarios()
                pass
