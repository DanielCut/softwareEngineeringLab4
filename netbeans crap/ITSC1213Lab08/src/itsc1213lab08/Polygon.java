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
public interface Polygon {
    public double computeArea();
    public double computePerimeter();
    public void movePoints(double delta_x, double delta_y);
    public String toString();
}

