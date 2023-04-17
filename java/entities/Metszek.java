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
public class Metszek implements java.io.Serializable {

    // Az aktuális pont nyíróerőértéke(0),nyomatéki értéke(1), A(2),Ix(3),Kx(4),Sx(5),v(6), Tau(7), Szigma(8), Szigma_ö(9), elfordulása(10), lehajlása(11)+ metszékkijelzés(12) + Átmeneti tároló a munkamódszerhez (13)   
    
    private float hely;
    private float nyiroero;
    private float nyomatek;
    private float szigma;
    private float tau;
    private float osszehasonlito_szigma;
    private float lehajlas;
    private float szogfordulas;
    // A keresztmetszeti jellemzők
    private float A;
    private float Ix;
    private float Kx;
    private float Sx;
    private float v;
    // A képernyőn lévő metszéki értékek
    private int nyiroero_metszek;
    private int nyomateki_metszek;
    private int szigma_metszek;
    private int tau_metszek;
    private int osszehasonlito_szigma_metszek;
    private int lehajlas_metszek;
    private int szogfordulas_metszek;
    // A kijelzés státusza
    private int kijelzes;

    public Metszek() {
    }
    
    public float getHely() {
        return hely;
    }

    public void setHely(float hely) {
        this.hely = hely;
    }

    public float getNyiroero() {
        return nyiroero;
    }

    public void setNyiroero(float nyiroero) {
        this.nyiroero = nyiroero;
    }

    public float getNyomatek() {
        return nyomatek;
    }

    public void setNyomatek(float nyomatek) {
        this.nyomatek = nyomatek;
    }

    public float getSzigma() {
        return szigma;
    }

    public void setSzigma(float szigma) {
        this.szigma = szigma;
    }

    public float getTau() {
        return tau;
    }

    public void setTau(float tau) {
        this.tau = tau;
    }

    public float getOsszehasonlito_szigma() {
        return osszehasonlito_szigma;
    }

    public void setOsszehasonlito_szigma(float osszehasonlito_szigma) {
        this.osszehasonlito_szigma = osszehasonlito_szigma;
    }

    public float getLehajlas() {
        return lehajlas;
    }

    public void setLehajlas(float lehajlas) {
        this.lehajlas = lehajlas;
    }

    public float getSzogfordulas() {
        return szogfordulas;
    }

    public void setSzogfordulas(float szogfordulas) {
        this.szogfordulas = szogfordulas;
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

    public int getNyiroero_metszek() {
        return nyiroero_metszek;
    }

    public void setNyiroero_metszek(int nyiroero_metszek) {
        this.nyiroero_metszek = nyiroero_metszek;
    }

    public int getNyomateki_metszek() {
        return nyomateki_metszek;
    }

    public void setNyomateki_metszek(int nyomateki_metszek) {
        this.nyomateki_metszek = nyomateki_metszek;
    }

    public int getSzigma_metszek() {
        return szigma_metszek;
    }

    public void setSzigma_metszek(int szigma_metszek) {
        this.szigma_metszek = szigma_metszek;
    }

    public int getTau_metszek() {
        return tau_metszek;
    }

    public void setTau_metszek(int tau_metszek) {
        this.tau_metszek = tau_metszek;
    }

    public int getOsszehasonlito_szigma_metszek() {
        return osszehasonlito_szigma_metszek;
    }

    public void setOsszehasonlito_szigma_metszek(int osszehasonlito_szigma_metszek) {
        this.osszehasonlito_szigma_metszek = osszehasonlito_szigma_metszek;
    }

    public int getLehajlas_metszek() {
        return lehajlas_metszek;
    }

    public void setLehajlas_metszek(int lehajlas_metszek) {
        this.lehajlas_metszek = lehajlas_metszek;
    }

    public int getSzogfordulas_metszek() {
        return szogfordulas_metszek;
    }

    public void setSzogfordulas_metszek(int szogfordulas_metszek) {
        this.szogfordulas_metszek = szogfordulas_metszek;
    }

    public int getKijelzes() {
        return kijelzes;
    }

    public void setKijelzes(int kijelzes) {
        this.kijelzes = kijelzes;
    }

    
}
