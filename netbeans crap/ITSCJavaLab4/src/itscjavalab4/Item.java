/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itscjavalab4;

/**
 *
 * @author Daniel Cutler
 */
public class Item 
{
    
    public String name;
    
    public double price;
    
    //constructor to take in input
    public Item(String itemName, double itemPrice)
    {
        name = itemName;
        price = itemPrice;
        
    }
    
    //getter methods
    public String getName()
    {
        return name;
    }
    
    public double getPrice()
    {
        return price;
    }
    
    
    //setter methods
    public void setName(String setName)
    {
        name = setName;
    }
    
    public void setPrice(double setPrice)
    {
        price = setPrice;
    }
    
    public String toString()
    {
        return (name + ": " + price);
    }
    
    
}
