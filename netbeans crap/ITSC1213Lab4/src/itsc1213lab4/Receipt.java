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
public class Receipt {

    private Transaction user;

    public Transaction getUser() {
        return user;
    }

    public Receipt(Transaction t) {
        user = t;
    }

    public String getReceiptString() {
        double totalCash=0;
        double totalCredit=0;
        double totalDebit=0;
        double totalCheck=0;
        for(Payment p: user.getPayments()){
            switch(p.getType())
            {
                case CASH:
                totalCash+=p.getAmount();
                break;
                case CREDIT_CARD:
                totalCredit+=p.getAmount();
                break;
                case DEBIT_CARD:
                totalDebit+=p.getAmount();
                break;
                case CHECK:
                totalCheck+=p.getAmount();
                break;
            }
        }
        String cash = "";
        if(totalCash>0.0)
            cash=String.format("Cash:    \t%f%n", totalCash);
        String credit = "";
        if(totalCredit>0.0)
            credit=String.format("Credit:  \t%f%n", totalCredit);
        String debit = "";
        if(totalDebit>0.0)
            debit=String.format("Debit:   \t%f%n", totalDebit);
        String check = "";
        if(totalCheck>0.0)
            check=String.format("Check:   \t%f%n", totalCheck);
            
        
        String userItems="";
         for(Item i: user.getItems())
        {
            userItems +=(i.toString()+"\n");
        }
        return String.format("%s---------------------------------------------%n"
                + "Subtotal:\t%f%n"
                + "Tax:     \t%f%n"
                + "Total:   \t%f%n"
                + "%s%s%s%s",
                userItems,user.computeSubTotal(),user.computeTax(), user.computeTotal(),
                cash, credit, debit, check);

    }

}
