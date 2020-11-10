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
public abstract class Octagon implements Polygon {
    public Octagon(Side[] sides) {
        Side[] s = sides;
    }
    
    @Override
    public double computeArea() {
        return (2*(1+Math.sqrt(2))*Math.pow(s[0].getLength(),2.0));
    }
}
