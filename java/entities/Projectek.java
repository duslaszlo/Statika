package Entities;
// Generated 2014.03.09. 21:55:51 by Hibernate Tools 3.6.0


import java.util.Date;

/**
 * Projectek generated by hbm2java
 */
public class Projectek  implements java.io.Serializable {


     private Integer id;
     private String projekt;
     private String megrendelo;
     private String leiras;
     private String aktiv;
     private Date felvitel;

    public Projectek() {
    }

    public Projectek(String projekt, String megrendelo, String leiras, String aktiv, Date felvitel) {
       this.projekt = projekt;
       this.megrendelo = megrendelo;
       this.leiras = leiras;
       this.aktiv = aktiv;
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
    public String getMegrendelo() {
        return this.megrendelo;
    }
    
    public void setMegrendelo(String megrendelo) {
        this.megrendelo = megrendelo;
    }
    public String getLeiras() {
        return this.leiras;
    }
    
    public void setLeiras(String leiras) {
        this.leiras = leiras;
    }
    public String getAktiv() {
        return this.aktiv;
    }
    
    public void setAktiv(String aktiv) {
        this.aktiv = aktiv;
    }
    public Date getFelvitel() {
        return this.felvitel;
    }
    
    public void setFelvitel(Date felvitel) {
        this.felvitel = felvitel;
    }




}

