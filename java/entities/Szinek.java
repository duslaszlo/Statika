package Entities;
// Generated 2014.11.11. 22:20:10 by Hibernate Tools 4.3.1


import java.util.Date;

/**
 * Szinek generated by hbm2java
 */
public class Szinek  implements java.io.Serializable {


     private Integer id;
     private String szinnev;
     private int r;
     private int g;
     private int b;
     private Date felvitel;

    public Szinek() {
    }

    public Szinek(String szinnev, int r, int g, int b, Date felvitel) {
       this.szinnev = szinnev;
       this.r = r;
       this.g = g;
       this.b = b;
       this.felvitel = felvitel;
    }
   
    public Integer getId() {
        return this.id;
    }
    
    public void setId(Integer id) {
        this.id = id;
    }
    public String getSzinnev() {
        return this.szinnev;
    }
    
    public void setSzinnev(String szinnev) {
        this.szinnev = szinnev;
    }
    public int getR() {
        return this.r;
    }
    
    public void setR(int r) {
        this.r = r;
    }
    public int getG() {
        return this.g;
    }
    
    public void setG(int g) {
        this.g = g;
    }
    public int getB() {
        return this.b;
    }
    
    public void setB(int b) {
        this.b = b;
    }
    public Date getFelvitel() {
        return this.felvitel;
    }
    
    public void setFelvitel(Date felvitel) {
        this.felvitel = felvitel;
    }




}


