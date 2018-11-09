from mipaquete.modelo import *
e=Empleado()
e.agregar_nombre("luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("1110001")
print(e.presentar_datos())

print("\nEmpleado Por Horas:\n")

e1=EmpleadoPorHoras()
nombre=input("Ingrese el nomnre: ")
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.agregar_cedula("112233")
e1.agregar_numero_horas(20.2)
e1.agregar_valor_hora(15)
print(e1.presentar_datos())


