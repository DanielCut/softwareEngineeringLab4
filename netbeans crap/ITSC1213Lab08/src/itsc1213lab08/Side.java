package itsc1213lab08;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author dcutler3
 */
public class Side {
    private Vertex v_start;
    private Vertex v_end;
    private double length;

    public Side(Vertex one, Vertex two){
    one = v_start;
    two = v_end;
    
    length = Math.sqrt((two.getX() - one.getX())*(two.getX() - one.getX()) + (two.getY() - one.getY())*(two.getY() - one.getY()));
}

    /**
     * @return the v_start
     */
    public Vertex getV_start() {
        return v_start;
    }

    /**
     * @param v_start the v_start to set
     */
    public void setV_start(Vertex v_start) {
        this.v_start = v_start;
    }

    /**
     * @return the v_end
     */
    public Vertex getV_end() {
        return v_end;
    }

    /**
     * @param v_end the v_end to set
     */
    public void setV_end(Vertex v_end) {
        this.v_end = v_end;
    }

    /**
     * @return the length
     */
    public double getLength() {
        return length;
    }

    /**
     * @param length the length to set
     */
    public void setLength(double length) {
        this.length = length;
    }
 
    public String toString(){
        return("V_start: " + v_start.toString() + " V_end: " + v_end.toString() + " Length: " + length);
    }
} 

