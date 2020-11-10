package itsc1212lab11;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class Main {

    public static void main(String[] args) {
       
        CalculatorGUI calculatorGUI = new CalculatorGUI();
        
        calculatorGUI.pack();
        calculatorGUI.setVisible(true);
    }
    
}
