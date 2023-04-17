package Entities;
// Generated 2014.03.09. 21:55:51 by Hibernate Tools 3.6.0


import java.util.Date;

/**
 * KonturE generated by hbm2java
 */
public class KonturE  implements java.io.Serializable {


     private Integer id;
     private String nev;
     private int vonal;
     private int sorszam;
     private int jelleg;
     private float x1;
     private float y1;
     private float x2;
     private float y2;
     private float r1;
     private float r2;
     private int irany;
     private Date felvitel;

    public KonturE() {
    }

    public KonturE(String nev, int vonal, int sorszam, int jelleg, float x1, float y1, float x2, float y2, float r1, float r2, int irany, Date felvitel) {
       this.nev = nev;
       this.vonal = vonal;
       this.sorszam = sorszam;
       this.jelleg = jelleg;
       this.x1 = x1;
       this.y1 = y1;
       this.x2 = x2;
       this.y2 = y2;
       this.r1 = r1;
       this.r2 = r2;
       this.irany = irany;
       this.felvitel = felvitel;
    }
   
    public Integer getId() {
        return this.id;
    }
    
    public void setId(Integer id) {
        this.id = id;
    }
    public String getNev() {
        return this.nev;
    }
    
    public void setNev(String nev) {
        this.nev = nev;
    }
    public int getVonal() {
        return this.vonal;
    }
    
    public void setVonal(int vonal) {
        this.vonal = vonal;
    }
    public int getSorszam() {
        return this.sorszam;
    }
    
    public void setSorszam(int sorszam) {
        this.sorszam = sorszam;
    }
    public int getJelleg() {
        return this.jelleg;
    }
    
    public void setJelleg(int jelleg) {
        this.jelleg = jelleg;
    }
    public float getX1() {
        return this.x1;
    }
    
    public void setX1(float x1) {
        this.x1 = x1;
    }
    public float getY1() {
        return this.y1;
    }
    
    public void setY1(float y1) {
        this.y1 = y1;
    }
    public float getX2() {
        return this.x2;
    }
    
    public void setX2(float x2) {
        this.x2 = x2;
    }
    public float getY2() {
        return this.y2;
    }
    
    public void setY2(float y2) {
        this.y2 = y2;
    }
    public float getR1() {
        return this.r1;
    }
    
    public void setR1(float r1) {
        this.r1 = r1;
    }
    public float getR2() {
        return this.r2;
    }
    
    public void setR2(float r2) {
        this.r2 = r2;
    }
    public int getIrany() {
        return this.irany;
    }
    
    public void setIrany(int irany) {
        this.irany = irany;
    }
    public Date getFelvitel() {
        return this.felvitel;
    }
    
    public void setFelvitel(Date felvitel) {
        this.felvitel = felvitel;
    }




}

