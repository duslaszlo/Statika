package Entities;
// Generated 2014.03.09. 21:55:51 by Hibernate Tools 3.6.0

import java.util.Date;

/**
 * Osszetett generated by hbm2java
 */
public class Osszetett implements java.io.Serializable {

    private Integer id;
    private String ossznev;
    private String nev;        // Az alkotó profil neve
    private float diffx;       // Az X-irányú eltolás mértéke
    private float diffy;       // Az Y-irányú eltolás mértéke
    private int szog;          // A forgatás mértéke
    private int mirrorx;       // Az X-irányú tükrözés (1-> igen)
    private int mirrory;       // Az Y-irányú tükrözés (1-> igen)
    private int bazis;         // A bázis kijelzése (1-> igen)
    private String hiba;       // Az átfedés jelzése (H-átfedés van)
    private Date felvitel;

    public Osszetett() {
    }

    public Osszetett(String ossznev, String nev, float diffx, float diffy, int szog, int mirrorx, int mirrory, int bazis,String hiba, Date felvitel) {
        this.ossznev = ossznev;
        this.nev = nev;
        this.diffx = diffx;
        this.diffy = diffy;
        this.szog = szog;
        this.mirrorx = mirrorx;
        this.mirrory = mirrory;
        this.bazis = bazis;
        this.hiba = hiba;
        this.felvitel = felvitel;
    }

    public Integer getId() {
        return this.id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getOssznev() {
        return this.ossznev;
    }

    public void setOssznev(String ossznev) {
        this.ossznev = ossznev;
    }

    public String getNev() {
        return this.nev;
    }

    public void setNev(String nev) {
        this.nev = nev;
    }

    public float getDiffx() {
        return this.diffx;
    }

    public void setDiffx(float diffx) {
        this.diffx = diffx;
    }

    public float getDiffy() {
        return this.diffy;
    }

    public void setDiffy(float diffy) {
        this.diffy = diffy;
    }

    public int getSzog() {
        return this.szog;
    }

    public void setSzog(int szog) {
        this.szog = szog;
    }

    public int getMirrorx() {
        return this.mirrorx;
    }

    public void setMirrorx(int mirrorx) {
        this.mirrorx = mirrorx;
    }

    public int getMirrory() {
        return this.mirrory;
    }

    public void setMirrory(int mirrory) {
        this.mirrory = mirrory;
    }

    public int getBazis() {
        return this.bazis;
    }

    public void setBazis(int bazis) {
        this.bazis = bazis;
    }

    public Date getFelvitel() {
        return this.felvitel;
    }

    public String getHiba() {
        return hiba;
    }

    public void setHiba(String hiba) {
        this.hiba = hiba;
    }        
    
    public void setFelvitel(Date felvitel) {
        this.felvitel = felvitel;
    }

}
