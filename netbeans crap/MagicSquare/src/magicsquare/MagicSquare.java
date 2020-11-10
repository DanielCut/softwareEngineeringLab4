/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package magicsquare;

import java.util.Arrays;
import java.io.*;
import java.util.Scanner;

/**
 *
 * @author Daniel Cutler
 */
public class MagicSquare {

    /**
     * @param args the command line arguments
     */
    private static int order;

    public static void main(String[] args) throws FileNotFoundException {

        int[][] array = readFile();
        int[][] arrayT = transpose(array);
        int reference = rowSum(array[0]);
        boolean isMagic = true;
        String answer = "";

        for (int i = 0; i < array.length; i++) {
            if (rowSum(array[i]) != reference || rowSum(arrayT[i]) != reference) {
                isMagic = false;
            }
        }
        
        if(isIntegerUnique(array)){
            isMagic = true;
        } else {
            isMagic = false;
        }

        if (diagonalSum(array, true) != reference || diagonalSum(array, false) != reference) {
            isMagic = false;
        }

        if (isMagic == true) {
            answer = "is a magic square.";
        } else {
            answer = "is not a magic square.";
        }
        if (isMagic == true) {
            System.out.println("The combination of numbers " + (Arrays.deepToString(array)) + "is a magic square order of " + array.length + ". The magic constant is " + reference + ".");

        } else {
            System.out.println("The combination of numbers " + (Arrays.deepToString(array)) + answer);
        }
    }

    public static int[][] readFile() throws FileNotFoundException {
        System.out.println("input file name");
        Scanner input = new Scanner(System.in);
        File file = new File(input.nextLine());
        input = new Scanner(file);
        String s = "";
        while (input.hasNextLine()) {
            s += input.nextLine();
        }
        order = (int) Math.sqrt(s.replaceAll(" ", "").length());
        int[][] matrix = new int[order][order];

        String[] arr = s.split(" ", 0);
        System.out.println(arr.length);
        int j = 0;
        for (int i = 0; i < order; i++) {
            for (int n = 0; n < order; n++) {
                matrix[i][n] = Integer.parseInt(arr[j]);
                j++;
            }
        }
        return matrix;
    }

    public static int[][] transpose(int array[][]) {
        int[][] temp = new int[array.length][array.length];
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                temp[j][i] = array[i][j];
            }
        }
        return temp;
    }

    public static int rowSum(int array[]) {
        int total = 0;

        for (int i = 0; i < array.length; i++) {
            total += array[i];
        }
        return total;
    }

    public static int diagonalSum(int array[][], boolean flip) {
        int total = 0;

        if (flip == true) {
            for (int i = 0; i < array.length; i++) {
                total += array[i][i];
            }
        } else {
            for (int i = 0; i < array.length; i++) {
                total += array[i][array.length - i - 1];
            }
        }
        return total;
    }

    public static boolean isIntegerUnique(int[][] arr) {
        boolean[] unique = new boolean[arr.length * arr[0].length + 1];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                if (unique[arr[i][j]]) {
                    return false;
                }
                unique[arr[i][j]] = true;
            }
        }
        return true;
    }
}
