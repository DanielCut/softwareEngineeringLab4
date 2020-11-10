package itsc1213lab10;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author dcutler3
 */
public class TrithemiusCipher implements Cipher {

    private int shift;
    private char[] alpha = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V',
        'W', 'X', 'Y', 'Z'};

    public TrithemiusCipher(int s) {
        this.shift = s;
    }

    public String encrypt(String s) {
        String encrypted = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ') {
                shift = i;
                encrypted += (charToIndex(s.charAt(i)) + shift);
            } else {
                shift = 0;
            }
        }
        return encrypted;
    }

    public String decrypt(String s) {

    }

    public int charToIndex(char c) {
        int result = (int) c;
        int lowerCase = 97;
        int upperCase = 65;
        if (result <= 122 && result >= 97) {
            result -= lowerCase;
        } else if (result >= 65 && result <= 90) {
            result -= upperCase;
        }
        return result;
    }
}
