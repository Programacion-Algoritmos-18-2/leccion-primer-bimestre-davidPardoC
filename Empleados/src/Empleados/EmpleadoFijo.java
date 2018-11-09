/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Empleados;

/**
 *
 * @author David Pardo
 */
public class EmpleadoFijo extends Empleado {
    //atributos
    static int sueldo_fijo;
    static double descuento;
    //constructor
    public EmpleadoFijo(String n, String a, String c, int co){
    super(n,a,c,co);
    }
    //getters y setters
    public static int getSueldo_fijo() {
        return sueldo_fijo;
    }

    public static void setSueldo_fijo(int s) {
        sueldo_fijo = s;
    }

    public static double getDescuento() {
        return descuento;
    }

    public static void setDescuento(double d) {
        descuento = d;
    }
    //calcula sueldo
    public static double calcular_sueldo(){
    return (sueldo_fijo+comision_fija)+((sueldo_fijo+comision_fija)*(descuento/100));
    }
    //presentar datos
   @Override
    public String toString(){
    
        return String.format("Iformacion de %s %s\nCedula:%S\nSueldo Final:%s",obtener_nombre(),obtener_apellido(),obtener_apellido(),calcular_sueldo());
     }
}
