package Entities;
// Generated 2014.03.10. 23:02:29 by Hibernate Tools 3.6.0



/**
 * Csomopont generated by hbm2java
 */
public class Csomopont  implements java.io.Serializable {


     private Integer id;
     private String projekt;
     private String azonosito;
     private int csomopont;
     private float x;
     private float y;
     private float z;

    public Csomopont() {
    }

    public Csomopont(String projekt, String azonosito, int csomopont, float x, float y, float z) {
       this.projekt = projekt;
       this.azonosito = azonosito;
       this.csomopont = csomopont;
       this.x = x;
       this.y = y;
       this.z = z;
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
    public int getCsomopont() {
        return this.csomopont;
    }
    
    public void setCsomopont(int csomopont) {
        this.csomopont = csomopont;
    }
    public float getX() {
        return this.x;
    }
    
    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return this.y;
    }
    
    public void setY(float y) {
        this.y = y;
    }
    public float getZ() {
        return this.z;
    }
    
    public void setZ(float z) {
        this.z = z;
    }




}


