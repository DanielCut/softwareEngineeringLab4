/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itscjavalab4;

import java.util.ArrayList;

public class Receipt {

    private Transaction member;

    private ArrayList<Item> itemArray = new ArrayList<Item>();

    public Receipt(Transaction t) {
        member = t;
    }

    //getter method
    public Transaction getTransaction() {
        return member;
    }

    public double computeSubTotal() {
        double subtotal = 0.0;
        for (int i = 0; i < itemArray.size(); i++) {
            subtotal += itemArray.get(i).price;
        }
        return subtotal;
    }

    public double computeTax() {
        double stateTax = 0.07;
        double tax = computeSubTotal() + stateTax;
        return tax;
    }

    public double computeTotal() {
        return this.computeSubTotal() + this.computeTax();
    }

    public void getReceiptString(ArrayList<Item> newList) {
        double subtotal = computeSubTotal();
        double tax = computeTax();
        String msg = "";
        for (int i = 0; i < newList.size(); i++) {
            msg += newList.get(i).name + ": " + newList.get(i).price + "\n";
            subtotal += newList.get(i).price;
        }
        msg += "---------------------------------------------\n";
        msg += "Subtotal:\t" + subtotal + "\n";
        msg += "Tax: \t \t" + tax * (subtotal) + "\n";
        msg += "Total:\t \t" + (subtotal + tax);
        System.out.println(msg);
    }
}
