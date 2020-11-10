package itsc1212lab11;

import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.LayoutManager;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class CalculatorGUI extends JFrame implements ActionListener {
private JLabel calculateLabel;
private JButton calculateButton;
private JTextField userInputA;
private JTextField userInputB;
private JTextField result;

public CalculatorGUI(){
    
    setTitle("CalculatorGUI");
    setLayout(new GridBagLayout());
    GridBagConstraints LayoutConst = new GridBagConstraints();
    GridBagConstraints gridx = new GridBagConstraints();
    GridBagConstraints gridy = new GridBagConstraints();
    LayoutConst.gridx = 0;
    LayoutConst.gridy = 0;
    LayoutConst.insets = new Insets(10,10,10,10);
    calculateLabel = new JLabel("Calculate");
    add(calculateLabel, LayoutConst);
    
    GridBagConstraints positionConst = new GridBagConstraints();
    
    calculateButton = new JButton("Add");
    calculateButton.addActionListener(this);
    positionConst.gridx = 0;
    positionConst.gridy = 2;
    positionConst.insets = new Insets(10,10,10,10);
    add(calculateButton, positionConst);
    
    userInputA = new JTextField(15);
    userInputA.setEditable(true);
    userInputA.setText("Enter A number");
    positionConst.gridx = 0;
    positionConst.gridy = 1;
    userInputA.setPreferredSize(new Dimension(100,20));
    userInputA.setMinimumSize(userInputA.getPreferredSize());
    add(userInputA, positionConst);
    
    userInputB = new JTextField(15);
    userInputB.setEditable(true);
    userInputB.setText("Enter A number");
    positionConst.gridx = 1;
    positionConst.gridy = 1;
    userInputB.setPreferredSize(new Dimension(100,20));
    userInputB.setMinimumSize(userInputA.getPreferredSize());
    add(userInputB, positionConst);
    
    result = new JTextField(15);
    result.setEditable(true);
    result.setText("");
    positionConst.gridx = 1;
    positionConst.gridy = 2;
    result.setPreferredSize(new Dimension(100,20));
    result.setMinimumSize(userInputA.getPreferredSize());
    add(result, positionConst);

}


public void actionPerformed (ActionEvent e){

calculateLabel.setText("Button Pressed");  
String userInput1;
String userInput2;
int user1;
int user2;
userInput1 = userInputA.getText();
userInput2 = userInputB.getText();

user1 = Integer.parseInt(userInput1);
user2 = Integer.parseInt(userInput2);

result.setText(Integer.toString(user1 + user2));

}



}
