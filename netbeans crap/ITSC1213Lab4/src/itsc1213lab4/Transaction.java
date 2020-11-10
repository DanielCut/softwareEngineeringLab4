/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itsc1213lab4;

/**
 * @author Sinclair
 */
import java.util.*;

public class Transaction {

    private ArrayList<Item> itemList = new ArrayList<Item>();
    private ArrayList<Payment> payments = new ArrayList<Payment>();
    private double subTotal;
    private double tax;
    private double total;
    private double change;

    //CONSTRUCTOR
    public Transaction(ArrayList<Item> list) {
        itemList = list;
    }

    //GETTERS
    public ArrayList<Item> getItems() {
        return itemList;
    }
    public ArrayList<Payment> getPayments() {
        return payments;
    }

    public double getSubTotal() {
        return subTotal;
    }

    public double getTotal() {
        return total;
    }

    public double getTax() {
        return tax;
    }

    public double getChange() {
        return change;
    }

    //SETTERS
    public void setItem(int index, Item item) {
        itemList.set(index, item);
    }

    public void setSubTotal(double d) {
        subTotal = d;
    }

    public void setTotal(double d) {
        total = d;
    }

    public void setTax(double d) {
        tax = d;
    }

    public void change(double d) {
        change = d;
    }

    public double computeSubTotal() {
        double sum = 0;
        for (Item n : itemList) {
            sum += n.getPrice();

        }
        this.subTotal = sum;
        return subTotal;
    }

    public double computeTax() {
        double tax = (computeSubTotal() * 0.07);
        this.tax = tax;
        return tax;
    }

    public double computeTotal() {
        double total = (computeSubTotal() + computeTax());
        this.total = total;
        return total;
    }

    public void takePayment() {
        Scanner input = new Scanner(System.in);

        PaymentType type = null;
        double amount = 0.0;
        int option = 0;
        

        double paymentTotal = 0.0;
        for (Payment p : payments) {
            paymentTotal += p.getAmount();
        }
        
        while (paymentTotal < this.total){
            while(option < 1 || option > 4) 
            {
                //Ask for payment type while option is invalid
                System.out.println("Please enter a payment type:\n"
                        + "1. Cash\n"
                        + "2. Debit Card\n"
                        + "3. Credit Card\n"
                        + "4. Check");
                if (input.hasNextInt())
                {
                    option = input.nextInt();
                    switch (option){
                        case 1: 
                            type=PaymentType.CASH;
                            break;
                        case 2: 
                            type=PaymentType.DEBIT_CARD;
                            break;
                        case 3: 
                            type=PaymentType.CREDIT_CARD;
                            break;
                        case 4: 
                            type=PaymentType.CHECK;
                            break;
                        default:
                            System.out.println("Please enter a VALID Payment type\n"
                                    + "1. Cash\n"
                                    + "2. Debit Card\n"
                                    + "3. Credit Card\n"
                                    + "4. Check");
                    
                    }
                }
                else{
                    input.next();
                    System.out.println("Please enter a VALID Payment type\n"
                            + "1. Cash\n"
                            + "2. Debit Card\n"
                            + "3. Credit Card\n"
                            + "4. Check");
                }
            }
            while(amount<=0.0){
                System.out.println("Please enter amount to pay");
                if(input.hasNextDouble()){
                    amount = input.nextDouble();
                    if(amount <=0.0)
                    {
                        System.out.println("Please enter a VALID amount");
  
                    }
                }
                else{
                    input.next();
                    System.out.println("Please enter a VALID amount");
                }
            }
              payments.add(new Payment(type, amount));
              
              paymentTotal+= amount;
              System.out.println("Total is now: " + (this.total-paymentTotal));
              
              type=null;
              option=0;
              amount=0.0;
        }
    }
    
}
