/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package itsc1213lab08;

/**
 *
 * @author dcutler3
 */
public class Vertex {
    private double x;
    private double y;

    public Vertex(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }
    
    public String toString(){
        return ("("+this.getX() + "," + this.getY() + ")");
                
    }
}

