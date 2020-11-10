/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itsc1213lab09;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author dcutler3
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        divideUserInput();
    }
    
    

    public static void addUserInput() throws NegativeNumberException {

        int sum = 0;
        Scanner sc = new Scanner(System.in);
        int userInput = 0;
        int userInput1 = 0;
        while (true) {
            try {
                System.out.println("please enter integer");
                userInput = sc.nextInt();
                break;
            } catch (InputMismatchException ne) {
                System.out.println("please enter integer");
                sc.next();
            } 
        NegativeNumberException e = new NegativeNumberException("Negative numbers are not allowed");
        throw e;
        }
         while (true) {
            try {
                System.out.println("please enter integer");
                userInput1 = sc.nextInt();
                throw  new NegativeNumberException("Negative numbers are not allowed");
                
            } catch (InputMismatchException ne) {
                System.out.println("please enter integer");
                sc.next();
            } catch (NegativeNumberException e){
                System.out.println("no negative number");
         
            }
            sum = userInput + userInput1;
        System.out.println("The sum is: " + sum);
        }
         
        
    }


public static void divideUserInput() {
  int divide = 0;
        Scanner sc = new Scanner(System.in);
        int userInput = 0;
        int userInput1 = 0;
        while (true) {
            try {
                System.out.println("please enter integer");
                userInput = sc.nextInt();
                break;
            } catch (InputMismatchException ne) {
                System.out.println("please enter integer");
                sc.next();
            }
        }
         while (true) {
            try {
                System.out.println("please enter integer");
                userInput1 = sc.nextInt();
                break;
            } catch (InputMismatchException ne) {
                System.out.println("please enter integer");
                sc.next();
            }
        }
        divide = userInput / userInput1;
        System.out.println("The quotient is: " + divide);
    }

public static void addFromFile(String filename){
    try{
        File myFile = new File(filename);
        Scanner sc = new Scanner(myFile);
    
        int integer1 = sc.nextInt();
        int integer2 = sc.nextInt();
        double sum = integer1 + integer2;
        System.out.println("Sum is: " + sum);
    }catch (InputMismatchException e){
        System.out.println("Input error");
    }catch (FileNotFoundException e){
        System.out.println("File not found");
    }catch (Exception e){
        System.out.println("Error");
    }
}

public static void divideFromFile(String filename){
    try{
        File myFile = new File(filename);
        Scanner sc = new Scanner(myFile);
    
        int integer1 = sc.nextInt();
        int integer2 = sc.nextInt();
        double sum = integer1 / integer2;
        System.out.println("Sum is: " + sum);
    }catch (InputMismatchException e){
        System.out.println("Input error");
    }catch (FileNotFoundException e){
        System.out.println("File not found");
    }catch (Exception e){
        System.out.println("Error");
    }
}

}




