/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itsc1213lab4;

//fields

public class Item 
{
    private String name;
    private double price;
    
    public Item(String name, double price)
    {
        this.name = name;
        this.price = price;
    }

    
    //GETTERS
    public String getName()
    {
        return name;
    }
    
    public double getPrice()
    {
        return price;
    }
    
    //SETTERS
    public void setName(String n)
    {
        name = n;
    }
    public void setPrice(double p)
    {
        price = p;
    }
    
    //To String
    public String toString()
    {
        return (name + ": " + price);
    }
}


