package Entities;
// Generated 2014.03.09. 21:55:51 by Hibernate Tools 3.6.0


import java.util.Date;

/**
 * Tartoerok generated by hbm2java
 */
public class Tartoerok  implements java.io.Serializable {


     private Integer id;
     private String projekt;
     private String tartonev;
     private int jelleg;
     private Float ertek;
     private Float hely;
     private Float hossz;
     private String szelveny;
     private Date felvitel;

    public Tartoerok() {
    }

	
    public Tartoerok(String projekt, String tartonev, int jelleg, String szelveny, Date felvitel) {
        this.projekt = projekt;
        this.tartonev = tartonev;
        this.jelleg = jelleg;
        this.szelveny = szelveny;
        this.felvitel = felvitel;
    }
    public Tartoerok(String projekt, String tartonev, int jelleg, Float ertek, Float hely, Float hossz, String szelveny, Date felvitel) {
       this.projekt = projekt;
       this.tartonev = tartonev;
       this.jelleg = jelleg;
       this.ertek = ertek;
       this.hely = hely;
       this.hossz = hossz;
       this.szelveny = szelveny;
       this.felvitel = felvitel;
    }
   
    public Integer getId() {
        return this.id;
    }
    
    public void setId(Integer id) {
        this.id = id;
    }
    public String getProjekt() {
        return this.projekt;
    }
    
    public void setProjekt(String projekt) {
        this.projekt = projekt;
    }
    public String getTartonev() {
        return this.tartonev;
    }
    
    public void setTartonev(String tartonev) {
        this.tartonev = tartonev;
    }
    public int getJelleg() {
        return this.jelleg;
    }
    
    public void setJelleg(int jelleg) {
        this.jelleg = jelleg;
    }
    public Float getErtek() {
        return this.ertek;
    }
    
    public void setErtek(Float ertek) {
        this.ertek = ertek;
    }
    public Float getHely() {
        return this.hely;
    }
    
    public void setHely(Float hely) {
        this.hely = hely;
    }
    public Float getHossz() {
        return this.hossz;
    }
    
    public void setHossz(Float hossz) {
        this.hossz = hossz;
    }
    public String getSzelveny() {
        return this.szelveny;
    }
    
    public void setSzelveny(String szelveny) {
        this.szelveny = szelveny;
    }
    public Date getFelvitel() {
        return this.felvitel;
    }
    
    public void setFelvitel(Date felvitel) {
        this.felvitel = felvitel;
    }




}

