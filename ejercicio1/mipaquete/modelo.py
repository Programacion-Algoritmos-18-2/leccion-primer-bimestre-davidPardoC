#Calse Empleado(Padre)
class Empleado(object):
    def __init__(self):
        self.nombre=" "
        self.apellido=" "
        self.cedula=" "
        self.comision_fija=300

    def agregar_comision(self, comision):
        self.comision_fija=comision

    def obtener_comision(self):
        return self.comision_fija

    def agregar_nombre(self, nombre):
        self.nombre=nombre

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, apellido):
        self.apellido=apellido

    def obtener_apellido(self):
        return self.apellido

    def agregar_cedula(self, cedula):
        self.cedula=cedula

    def obtener_cedula(self):
        return self.cedula

    def presentar_datos(self):
        cadena="Informacion de %s %s \n\t cedula %s"%(self.obtener_nombre(), self.obtener_apellido(), self.cedula)
        return cadena
#Calse EmpleadoPorHoras(Hija)
class EmpleadoPorHoras(Empleado):
    def __init__(self):
        super(EmpleadoPorHoras, self).__init__()
        self.num_Horas = 0
        self.valorHoras = 0

#getters y setters
    def agregar_numero_horas(self, h):
        self.num_Horas = h

    def obtener_num_horas(self):
        return self.num_Horas

    def agregar_valor_hora(self, v):
        self.valorHoras=v

    def obtener_valor_horas(self):
        return self.valorHoras
#calcula Sueldo
    def calcular_sueldo(self):
        sueldo = (self.num_Horas*self.valorHoras)+self.comision_fija
        return sueldo

    def presentar_datos(self):
        cadena="%s \n Numero horas: %s \n Valor Hora: %s \n Sueldo Final: %s"%(super(EmpleadoPorHoras, self).presentar_datos(), self.obtener_num_horas(), self.obtener_valor_horas(), self.calcular_sueldo())
        return cadena
#Clase EpleadoFijo(Hija)
class EmpleadoFijo(Empleado):
    def __init__(self):
        super(EmpleadoFijo, self). __init__()
        self.sueldofijo=0
        self.descuento_seguro=0

#getters y setters

    def agregar_sueldo_fijo(self, s):
        self.sueldofijo=s

    def obtener_sueldo_fijo(self):
        return self.sueldofijo

    def agregar_descuento(self, d):
        self.descuento_seguro=d

    def obtener_descuento(self):
        return self.descuento_seguro

#Clacula el sueldo

    def calcular_sueldo(self):
        sueldo = (self.comision_fija+self.sueldofijo)-((self.comision_fija+self.sueldofijo)*(self.descuento_seguro/100))+self.comision_fija
        return sueldo

    def presentar_datos(self):
        cadena="%s \n Sueldo Final: %s"%(super(EmpleadoFijo, self).presentar_datos(), self.calcular_sueldo())
        return cadena

#Clase EmpleadoSemnal(Hija)
class EmpleadoSemanal(Empleado):
    def __init__(self):
        super(EmpleadoSemanal, self).__init__()
        self.numero_semanas=0
        self.valor_semana=0

#Setters y Getters

    def agregar_numero_semanas(self, n):
        self.numero_semanas=n

    def obtener_numero_semanas(self):
        return self.numero_semanas

    def agregar_valor_semana(self, v):
        self.valor_semana=v

    def obtener_valor_semana(self):
        return self.valor_semana

#Calcula Sueldo Final

    def sueldo_final(self):
        sueldo=(self.valor_semana*self.numero_semanas)+self.comision_fija
        return sueldo

    def presentar_datos(self):
        cadena="%s \n Sueldo Final: %s"%(super(EmpleadoSemanal, self).presentar_datos(), self.sueldo_final())
        return cadena