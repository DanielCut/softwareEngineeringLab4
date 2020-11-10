/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itscjavalab4;

import java.util.ArrayList;

/**
 *
 * @author Daniel Cutler
 */
public class ITSCJavaLab4 {

    public static void main(String[] args) 
    {
        Item souljaGameHandheld = new Item("souljaBoyHandheld", 400.0);
        Item souljaPods = new Item("souljaPods", 500.0);
        Item souljaGameConsole = new Item ("souljaGameConsole", 1000.0);
        
        ArrayList<Item> newList = new ArrayList<Item>();
        newList.add(souljaGameHandheld);
        newList.add(souljaPods);
        newList.add(souljaGameConsole);
        
        System.out.println(souljaGameHandheld.toString());
        System.out.println(souljaPods.toString());
        System.out.println(souljaGameConsole.toString());
        
        Receipt receipt = new Receipt(new Transaction(newList));
        receipt.getReceiptString(newList);
    }
    
}
