package Entities;
// Generated 2014.03.09. 21:55:51 by Hibernate Tools 3.6.0

import java.util.Date;

/**
 * Tartok generated by hbm2java
 */
public class Tartok implements java.io.Serializable {

    private Integer id;
    private String projekt;
    private String tartonev;
    private int tipus;
    private float hossz;
    private float konzol1;
    private float konzol2;
    private String szelveny;
    private int aktiv;
    private String note;
    private Date felvitel;

    public Tartok() {
    }

    public Tartok(String projekt, String tartonev, int tipus, float hossz, float konzol1, float konzol2, String szelveny, int aktiv, String note, Date felvitel) {
        this.projekt = projekt;
        this.tartonev = tartonev;
        this.tipus = tipus;
        this.hossz = hossz;
        this.konzol1 = konzol1;
        this.konzol2 = konzol2;
        this.szelveny = szelveny;
        this.aktiv = aktiv;
        this.note = note;
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

    public int getTipus() {
        return this.tipus;
    }

    public void setTipus(int tipus) {
        this.tipus = tipus;
    }

    public float getHossz() {
        return this.hossz;
    }

    public void setHossz(float hossz) {
        this.hossz = hossz;
    }

    public float getKonzol1() {
        return this.konzol1;
    }

    public void setKonzol1(float konzol1) {
        this.konzol1 = konzol1;
    }

    public float getKonzol2() {
        return this.konzol2;
    }

    public void setKonzol2(float konzol2) {
        this.konzol2 = konzol2;
    }

    public String getSzelveny() {
        return this.szelveny;
    }

    public void setSzelveny(String szelveny) {
        this.szelveny = szelveny;
    }

    public int getAktiv() {
        return this.aktiv;
    }

    public void setAktiv(int aktiv) {
        this.aktiv = aktiv;
    }

    public String getNote() {
        return this.note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public Date getFelvitel() {
        return this.felvitel;
    }

    public void setFelvitel(Date felvitel) {
        this.felvitel = felvitel;
    }

}
