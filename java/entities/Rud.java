package Entities;
// Generated 2014.03.10. 23:02:29 by Hibernate Tools 3.6.0



/**
 * Rud generated by hbm2java
 */
public class Rud  implements java.io.Serializable {


     private Integer id;
     private String projekt;
     private String azonosito;
     private int kezdocsp;
     private int vegecsp;
     private float anyag;
     private int piros;
     private int zold;
     private int kek;
     private int vastagsag;
     private String szelveny;

    public Rud() {
    }

    public Rud(String projekt, String azonosito, int kezdocsp, int vegecsp, float anyag, int piros, int zold, int kek, int vastagsag, String szelveny) {
       this.projekt = projekt;
       this.azonosito = azonosito;
       this.kezdocsp = kezdocsp;
       this.vegecsp = vegecsp;
       this.anyag = anyag;
       this.piros = piros;
       this.zold = zold;
       this.kek = kek;
       this.vastagsag = vastagsag;
       this.szelveny = szelveny;
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
    public String getAzonosito() {
        return this.azonosito;
    }
    
    public void setAzonosito(String azonosito) {
        this.azonosito = azonosito;
    }
    public int getKezdocsp() {
        return this.kezdocsp;
    }
    
    public void setKezdocsp(int kezdocsp) {
        this.kezdocsp = kezdocsp;
    }
    public int getVegecsp() {
        return this.vegecsp;
    }
    
    public void setVegecsp(int vegecsp) {
        this.vegecsp = vegecsp;
    }
    public float getAnyag() {
        return this.anyag;
    }
    
    public void setAnyag(float anyag) {
        this.anyag = anyag;
    }
    public int getPiros() {
        return this.piros;
    }
    
    public void setPiros(int piros) {
        this.piros = piros;
    }
    public int getZold() {
        return this.zold;
    }
    
    public void setZold(int zold) {
        this.zold = zold;
    }
    public int getKek() {
        return this.kek;
    }
    
    public void setKek(int kek) {
        this.kek = kek;
    }
    public int getVastagsag() {
        return this.vastagsag;
    }
    
    public void setVastagsag(int vastagsag) {
        this.vastagsag = vastagsag;
    }
    public String getSzelveny() {
        return this.szelveny;
    }
    
    public void setSzelveny(String szelveny) {
        this.szelveny = szelveny;
    }




}


