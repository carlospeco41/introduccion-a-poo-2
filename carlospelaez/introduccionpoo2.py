class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")

class Salario:
    def __init__(self):
        self.salario = float(input("Ingrese el salario del empleado: "))

class Designacion(Empleado, Salario):
    def __init__(self):
        Empleado.__init__(self)
        Salario.__init__(self)
        self.cargo = None

    def asignar_cargo(self, cargo):
        self.cargo = cargo

# Verificación del código
objeto_designacion = Designacion()
print("El objeto tiene el método 'nombre':", hasattr(objeto_designacion, 'nombre'))
print("El objeto tiene el método 'salario':", hasattr(objeto_designacion, 'salario'))
