/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Empleados;

import java.util.Scanner;

/**
 *
 * @author David Pardo
 */
public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        //crea e
        Empleado e = new Empleado("Luis","Benitez","11100001",300);
        System.out.println("\tEmpleado\n\n"+e);
        System.out.println("\nEmpleado Horas\n");
        System.out.println("Ingresar el nombre: ");
        String nombre = leer.next();
        //crea e2
        EmpleadoHoras e2 = new EmpleadoHoras(nombre,"Andrade","112233",300);
        e2.agregar_num_horas(15);
        e2.agregar_valor_hora(20.2);
        System.out.println(e2);
        System.out.println("\nEmpleado Fijo\n");
        System.out.println("Ingrese la comision:");
        int comision = leer.nextInt();
        //crea e3
        EmpleadoFijo e3 = new EmpleadoFijo("Ana","Diaz","110011",comision);
        e3.setSueldo_fijo(3002);
        e3.setDescuento(10);
        System.out.println(e3);
        System.out.println("\nEmpleado  Semanal: ");
        //crea e4
        EmpleadoSemanal e4 = new EmpleadoSemanal("David","Pardo","1103315220",300);
        e4.setSemanas(4);
        e4.setValor_semana(120);
        System.out.println(e4);
    }
    
}
