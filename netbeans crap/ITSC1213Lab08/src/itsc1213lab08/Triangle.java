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
public class Triangle implements Polygon {

    private Side[] s = null;

    public Triangle(Side[] sides) {
        s = sides;
    }

    public Side[] getS() {
        return s;
    }

    public void setS(Side[] s) {
        this.s = s;
    }

    public double computeArea() {
        double temp = 0;
        for (int i = 0; i < s.length; i++) {
            temp = (int) s[i].getLength();
            return temp;
        }
        return temp;
    }

    public double computePerimeter() {
        double temp = s[0].getLength() * 3.0;
        return temp;
    }

    public void movePoints(double delta_x, double delta_y) {
        for (int i = 0; i < s.length; i++) {
            s[i].getV_start().setX(s[1].getV_start().getX());
            s[i].getV_start().setY(s[1].getV_start().getY());
            s[i].getV_end().setX(s[1].getV_end().getX());
            s[i].getV_end().setY(s[1].getV_end().getY());
        }
    }

    public String toString() {
        String temp = "";
        for (Side side : s) {
            temp += s.toString() + "\n";
        }
        return temp;
    }
}

