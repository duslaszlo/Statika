/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Entities;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author SD-LEAP
 */
public class Konturvonal implements java.io.Serializable {

    private int azonosito;   // Összetett szelvényeknél a szelvény sorszáma
    private String nev;      // A szelvény neve  (Összetett szelvenynel)
    private int vonal;       // A vonal sorszáma 1-külső, 2 vagy több -> belső
    // Átmeneti tárolók a forgatásnál
    private float x;
    private float y;
    // A pontsor pontjai
    List<Konturpont> konturpont = new ArrayList<>(); // A kontúrvonalak X,Y koordinátái    

    public Konturvonal() {
    }

    public int getAzonosito() {
        return azonosito;
    }

    public void setAzonosito(int azonosito) {
        this.azonosito = azonosito;
    }

    public String getNev() {
        return nev;
    }

    public void setNev(String nev) {
        this.nev = nev;
    }

    public int getVonal() {
        return vonal;
    }

    public void setVonal(int vonal) {
        this.vonal = vonal;
    }

    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public List<Konturpont> getKonturpont() {
        return konturpont;
    }

    public void setKonturpont(List<Konturpont> konturpont) {
        this.konturpont = konturpont;
    }

    /*public Konturpont getKeppont() {
        return keppont;
    }

    public void setKeppont(Konturpont keppont) {
        this.keppont = keppont;
    } */

    public void pontforgato(float szelesseg, float magassag, float forgatas) {
        double atfogo;
        float kozepx = szelesseg / 2;
        float kozepy = magassag / 2;
        double szog;                    // A forgatásnál az elfordítás szöge - átmeneti tároló
        szog = 0;
        atfogo = Math.sqrt(Double.parseDouble(String.valueOf((kozepx - x) * (kozepx - x) + (kozepy - y) * (kozepy - y))));
        if ((kozepx == x) && (kozepy > y)) {
            szog = Math.toRadians(90);
        } else if ((kozepx == x) && (kozepy < y)) {
            szog = Math.toRadians(270);
        } else if ((kozepy == y) && (kozepx > x)) {
            szog = Math.toRadians(180);
        } else if ((kozepy == y) && (kozepx < x)) {
            szog = 0;
        } else if ((y < kozepy) && (x > kozepx)) {
            szog = Math.asin((kozepy - y) / atfogo);
        } else if ((y < kozepy) && (x < kozepx)) {
            szog = Math.toRadians(90) + Math.asin((kozepx - x) / atfogo);
        } else if ((y > kozepy) && (x < kozepx)) {
            szog = Math.toRadians(180) + Math.asin((y - kozepy) / atfogo);
        } else if ((y > kozepy) && (x > kozepx)) {
            szog = Math.toRadians(270) + Math.asin((x - kozepx) / atfogo);
        }
        //System.out.println(" regiszog:" + (int)Math.toDegrees(szog) + " Elforgatás:" + forgatas);
        szog += Math.toRadians(forgatas + 90);
        //System.out.println(" ujszog:" + (int)Math.toDegrees(szog));    
        x = kozepx + Float.parseFloat(String.valueOf(Math.sin(szog) * atfogo));
        y = kozepy + Float.parseFloat(String.valueOf(Math.cos(szog) * atfogo));
    }

    public void pontgenerator(int j, int jelleg, float szelesseg, float magassag, float forgatas, float xx1, float xx2, float yy1, float yy2, float r1, float r2, int irany, float arany, int szorzo) {
        Konturpont keppont = new Konturpont();
        Konturpont keppont1 = new Konturpont();
        Integer pontszam=0;        
        if (jelleg == 1) {
            // egyenes vonalak
            if ((forgatas != 0) && (forgatas != 360)) {
                x = xx1;
                y = yy1;
                pontforgato(szelesseg, magassag, forgatas);
                xx1 = x;
                yy1 = y;
                x = xx2;
                y = yy2;
                pontforgato(szelesseg, magassag, forgatas);
                xx2 = x;
                yy2 = y;
            }
            if (j == 0) {
                keppont1.setX((int) (xx1 * arany * szorzo));
                keppont1.setY((int) (yy1 * arany * szorzo));
                konturpont.add(keppont1);
                pontszam++;
                /*System.out.println("Képpont:"+(konturpont.size()-1)+
                        " x:"+konturpont.get(konturpont.size()-1).getX()+
                        " y:"+konturpont.get(konturpont.size()-1).getY());*/
                
            }
            keppont.setX((int) (xx2 * arany * szorzo));
            keppont.setY((int) (yy2 * arany * szorzo));
            konturpont.add(keppont);
            pontszam++;
            //System.out.println("Képpont:"+(konturpont.size()-1)+" x:"+keppont.getX()+" y:"+keppont.getY());
        } else {
            // A görbe vonalak
            if ((forgatas != 0) && (forgatas != 360)) {
                x = xx1;
                y = yy1;
                pontforgato(szelesseg, magassag, forgatas);
                xx1 = x;
                yy1 = y;
                //System.out.println("I:" + i + " J:" + j + " Forgatás:" + forgatas + " r1_elötte:" + r1 + "  r2_elotte:" + r2);
                r1 -= forgatas;
                r2 -= forgatas;
                //System.out.println(" r1_utána:" + r1 + "  r2_utána:" + r2);
            }
            //System.out.println("X1:" + x1[j] + " y1:" + y1[j] + " X2:" + x2[j] + " y2:" + y2[j] + " kezdoszog:" + kezdoszog[j] + "  Végszög:" + vegszog[j] + "  Irány:" + irany[j]);
            if ((r1 == 0) && (r2 == 360)) {
                //Teljes kör                                
                for (int k = 0; k < 360; k++) {
                    Konturpont keppont2 = new Konturpont();
                    keppont2.setX((int) ((xx1 * szorzo + xx2 * szorzo * Math.cos(Math.toRadians(k))) * arany));
                    keppont2.setY((int) ((yy1 * szorzo + yy2 * szorzo * Math.sin(Math.toRadians(k))) * arany));
                    konturpont.add(keppont2);        
                    pontszam++;
                    //System.out.println(" szamlalo:" + szamlalo + " x1:" + x1[j] + " y1:" + y1[j]+ " x2:" + x2[j] + " y2:" + y2[j] +" arany:" + arany + " eltolasx:" + eltolasx+" pontx:"+pontokx[szamlalo]+" ponty:"+pontoky[szamlalo]);
                    //System.out.println(" k:" + k +" x1:"+ x1[j][i]+"  y1:"+ y1[j][i]+ " cos k*x2:" + (x1[j][i] + x2[j][i] * Math.cos(k * (Math.PI / 180)))+ " sin k*y2:" + (y1[j][i] + y2[j][i] * Math.sin(k * (Math.PI / 180))));
                }
            } else {
                if (irany == 1) {
                    // Az óra járásával megegyező irány (CW)
                    if (r2 < r1) {
                        r2 += 360;
                    }
                    for (int k = (int) r1; k < (int) r2; k++) {
                        Konturpont keppont2 = new Konturpont();
                        keppont2.setX((int) ((xx1 * szorzo + xx2 * szorzo * Math.cos(Math.toRadians(k))) * arany));
                        keppont2.setY((int) ((yy1 * szorzo + yy2 * szorzo * Math.sin(Math.toRadians(k))) * arany));
                        konturpont.add(keppont2);
                        pontszam++;
                        //System.out.println(" k:" + k + " x1:" + x1[j][i] + "  y1:" + y1[j][i] + " cos k*x2:" + (x1[j][i] + x2[j][i] * Math.cos(k * (Math.PI / 180))) + " sin k*y2:" + (y1[j][i] + y2[j][i] * Math.sin(k * (Math.PI / 180))));
                    }
                } else {
                    // Az óra járásával ellentétes irány (CCW)
                    if (r2 > r1) {
                        r2 -= 360;
                    }
                    //System.out.println(" kezdoszog:" + kezdoszog[j] + " vegszog:" + vegszog[j]);
                    for (int k = (int) r1; k > (int) r2; k--) {
                        Konturpont keppont2 = new Konturpont();
                        keppont2.setX((int) ((xx1 * szorzo + xx2 * szorzo * Math.cos(Math.toRadians(k))) * arany));
                        keppont2.setY((int) ((yy1 * szorzo + yy2 * szorzo * Math.sin(Math.toRadians(k))) * arany));
                        konturpont.add(keppont2);
                        pontszam++;
                        //System.out.println(" k:" + k + " x1:" + x1[j][i] + "  y1:" + y1[j][i] + " cos k*x2:" + (x1[j][i] + x2[j][i] * Math.cos(k * (Math.PI / 180))) + " sin k*y2:" + (y1[j][i] + y2[j][i] * Math.sin(k * (Math.PI / 180))));
                    }
                }
            } 
           /* konturpont.get(0).setX(konturpont.get(konturpont.size()-1).getX());
            konturpont.get(0).setX(konturpont.get(konturpont.size()-1).getX());*/
        }
        //System.out.println("A pontok száma:"+pontszam);
    }

}
