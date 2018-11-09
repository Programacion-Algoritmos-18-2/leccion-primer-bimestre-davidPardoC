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
public class Empleado {
    static String nombre,apellido, cedula;
    static int comision_fija;
    //constructor
    Empleado(String n, String a, String c, int co){
        nombre=n;
        apellido=a;
        cedula=c;
        comision_fija=co;
    }
    //getters y setters
    public static void agregar_nombre(String n){
        nombre = n;
    }
    public static String obtener_nombre(){
        return nombre;
    }
    public static void agregar_apellido(String a){
        apellido=a;
    }
    public static String obtener_apellido(){
        return apellido;
    }
    public static void agregar_cedula(String c){
        cedula=c;
    }
    public static String obtener_cedula(){
        return cedula;
    }
    public static void agregar_comision(int c){
        comision_fija=c;
    }
    public static int obtener_comision(){
        return comision_fija;
    }   
    //presentar datos
    @Override
    public String toString(){
    
        return String.format("Informacion de %s %S\nCedula: %s", obtener_nombre(), obtener_apellido(), obtener_cedula());
     }
}
