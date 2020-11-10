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
public class Payment {

    private PaymentType type;
    private double amount;

    //constructors
    public Payment(PaymentType type, double amount) {
        type = type;
        amount = amount;
    }

    public PaymentType getType() {
        return type;
    }

    public void setType(PaymentType type) {
        type = type;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        amount = amount;
    }
}
