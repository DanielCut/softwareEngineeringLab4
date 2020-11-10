/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itsc1213lab10;

/**
 *
 * @author dcutler3
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        TrithemiusCipher c = new TrithemiusCipher(0);
        System.out.println(c.encrypt("The encryption is working correctly"));
    }
    
}
