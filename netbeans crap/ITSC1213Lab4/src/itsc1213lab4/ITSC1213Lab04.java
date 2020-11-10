/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itsc1213lab4;

/**
 *
 * @author Sinclair
 */
import java.util.*;
public class ITSC1213Lab04 {

    
    public static void main(String[] args)
    {
        Item metro = new Item("Metro 2033", 50.25);
        Item redDead = new Item("Red Dead Redemption 2", 60.00);
        Item fallout76= new Item("Fallout 76" , 20.00);
        
        ArrayList<Item> buy = new ArrayList<Item>();
        buy.add(metro);
        buy.add(redDead);
        buy.add(fallout76);
        
        Transaction t = new Transaction(buy);
       
        Receipt log=new Receipt(t);
        System.out.println(log.getReceiptString());
        t.computeTotal();
        t.takePayment();
         System.out.println(log.getReceiptString());
    }
  
}
