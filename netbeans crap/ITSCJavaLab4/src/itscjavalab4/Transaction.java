/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itscjavalab4;

import java.util.ArrayList;


public class Transaction 
{
    private double subTotal = 0.0;
    private double tax = 0.0;
    private double total = 0.0;
    private double change = 0.0;
    
    private ArrayList<Item> itemArray = new ArrayList<Item>();
    
    //constructor for Transaction
    public Transaction(ArrayList<Item> list)
    {
        itemArray = list;
    }
    
    //getter and setter for the array
    public Item getArray(int index)
    {
        return itemArray.get(index);
    }
    
    public Item setArray(int index, Item item)
    {
        return itemArray.set(index, item);
    }
    
    
    //getter methods for the private double variables
    public double getSubTotal()
    {
        return subTotal;
    }
    
    public double getTax()
    {
        return tax;
    }
    
    public double getTotal()
    {
        return total;
    }
    
    public double getChange()
    {
        return change;
    }
    
    
    //setter methods for private double variables
    public void setSubTotal(double setSubTotal)
    {
        total = setSubTotal;
    }
    
    public void setTax(double setTax)
    {
        tax = setTax;
    }
    
    public void setTotal(double setTotal)
    {
        total = setTotal;
    }
    
    public void setChange(double setChange)
    {
        change = setChange;
    }
}
