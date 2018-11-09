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
public class EmpleadoSemanal extends Empleado{
    //atributos
   static int valor_semana, semanas;
   //constructor
    public EmpleadoSemanal(String n, String a, String c, int co){
    super(n,a,c,co);
    }
    public int getValor_semana() {
        return valor_semana;
    }

    public void setValor_semana(int valor_semana) {
        this.valor_semana = valor_semana;
    }

    public int getSemanas() {
        return semanas;
    }

    public void setSemanas(int semanas) {
        this.semanas = semanas;
    }
    //calcula sueldo
    public static int sueldo(){
    return (valor_semana*semanas)+comision_fija;
    }
    //presetar datos
    @Override
    public String toString(){
    
        return String.format("Informacion de %s %S\n Sueldo FInal: %s", obtener_nombre(), obtener_apellido(), sueldo());
     }
}
