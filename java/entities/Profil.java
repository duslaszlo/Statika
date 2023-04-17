/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Entities;

/**
 *
 * @author SD-LEAP
 */
public class Profil implements java.io.Serializable {

    // Az aktuális profil adatai: Szelvénynév,A,Ix,Kx,Sx,v, hely, hossz
    
    private String nev;
    // A keresztmetszeti jellemzők
    private float A;
    private float Ix;
    private float Kx;
    private float Sx;
    private float v;
    // A hossz értékek
    private float hely;
    private float hossz;

    public Profil() {
    }

    public String getNev() {
        return nev;
    }

    public void setNev(String nev) {
        this.nev = nev;
    }

    public float getA() {
        return A;
    }

    public void setA(float A) {
        this.A = A;
    }

    public float getIx() {
        return Ix;
    }

    public void setIx(float Ix) {
        this.Ix = Ix;
    }

    public float getKx() {
        return Kx;
    }

    public void setKx(float Kx) {
        this.Kx = Kx;
    }

    public float getSx() {
        return Sx;
    }

    public void setSx(float Sx) {
        this.Sx = Sx;
    }

    public float getV() {
        return v;
    }

    public void setV(float v) {
        this.v = v;
    }

    public float getHely() {
        return hely;
    }

    public void setHely(float hely) {
        this.hely = hely;
    }

    public float getHossz() {
        return hossz;
    }

    public void setHossz(float hossz) {
        this.hossz = hossz;
    }    

}
