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
public class EmpleadoHoras extends Empleado{
    //atributos
    static int num_horas; static double valor_hora;
    //cosntrucotr
    public EmpleadoHoras(String n, String a, String c, int co){
    super(n,a,c,co);
    }
    //getters y setters
    public static void agregar_num_horas(int n){
        num_horas=n;
    }
    public static int obtener_numero_horas(){
        return num_horas;
    }
    public static void agregar_valor_hora(double h){
        valor_hora=h;
    }
    public static double obtener_valor_hora(){
        return valor_hora;
    }
    //calcula sueldo
    public static double calcular_sueldo(){
        double sueldo=(num_horas*valor_hora)+comision_fija;
        return sueldo;
    }
    //presentar datos
    @Override
    public String toString(){
    
        return String.format("Informacion de %s %S\n Numero de horas: %s\nValor por hora: %s \nCedula: %s\nSueldo FInal: %s", obtener_nombre(), obtener_apellido(), obtener_cedula(),obtener_numero_horas(),obtener_valor_hora(),calcular_sueldo());
     }
}
