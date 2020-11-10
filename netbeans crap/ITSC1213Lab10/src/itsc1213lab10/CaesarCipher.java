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
public class CaesarCipher implements Cipher {

    private int shift;

    public CaesarCipher(int shift) {
        this.shift = shift;
    }
    
    public String encrypt(String s){
        this.shift = shift * -1;
        char[] result = s.toCharArray();
        for (int i = 0; i < result.length; i++) {
            if(result[i] != ' '){
            result[i] += shift;
            }
        }
        String shiftedResult = new String(result);
        return shiftedResult;
    }
    
    public String decrypt(String s){
        char[] result = s.toCharArray();
        for (int i = 0; i < result.length; i++) {
            if(result[i] != ' '){
            result[i] += shift;
            }
        }
        String shiftedResult = new String(result);
        return shiftedResult;
    }
}
