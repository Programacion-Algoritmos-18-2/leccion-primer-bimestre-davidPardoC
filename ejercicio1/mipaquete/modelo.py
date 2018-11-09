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

class EmpleadoPorHoras(Empleado):
    def __init__(self):
        super(EmpleadoPorHoras, self).__init__()
        self.num_Horas = 0
        self.valorHoras = 0

    def agregar_numero_horas(self, h):
        self.num_Horas = h

    def obtener_num_horas(self):
        return self.num_Horas

    def agregar_valor_hora(self, v):
        self.valorHoras=v

    def obtener_valor_horas(self):
        return self.valorHoras

    def calcular_sueldo(self):
        sueldo = (self.num_Horas*self.valorHoras)+self.comision_fija
        return sueldo

    def presentar_datos(self):
        cadena="%s \n Numero horas: %s \n Valor Hora: %s \n Sueldo Final: %s"%(super(EmpleadoPorHoras, self).presentar_datos(), self.obtener_num_horas(), self.obtener_valor_horas(), self.calcular_sueldo())
        return cadena