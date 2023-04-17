/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package Entities;

import java.awt.Color;
import java.awt.Stroke;

/**
 *
 * @author SD-LEAP
 */
public class Racstervezorud implements java.io.Serializable {
    
    private int szekcio;
    private int kijelzes;
    private int koz;
    private int tipus;
    private float hossz;
    private Stroke teljesvonal;      // A rajzolásnál a vonal vastagsága
    private Stroke szekciovonal;      // A rajzolásnál a vonal vastagsága
    private Color teljesszin;  // A teljes rajznál a vonal kijelzett színe
    private Color szekcioszin; // A szekciórajznál a vonal kijelzett színe
    Rud rud;

    public Racstervezorud() {
    }
    
    public int getSzekcio() {
        return szekcio;
    }

    public void setSzekcio(int szekcio) {
        this.szekcio = szekcio;
    }

    public int getKijelzes() {
        return kijelzes;
    }

    public void setKijelzes(int kijelzes) {
        this.kijelzes = kijelzes;
    }

    public int getKoz() {
        return koz;
    }

    public void setKoz(int koz) {
        this.koz = koz;
    }

    public int getTipus() {
        return tipus;
    }

    public void setTipus(int tipus) {
        this.tipus = tipus;
    }

    public float getHossz() {
        return hossz;
    }

    public void setHossz(float hossz) {
        this.hossz = hossz;
    }

    public Rud getRud() {
        return rud;
    }

    public void setRud(Rud rud) {
        this.rud = rud;
    }

    public Color getTeljesszin() {
        return teljesszin;
    }

    public void setTeljesszin(Color teljesszin) {
        this.teljesszin = teljesszin;
    }

    public Color getSzekcioszin() {
        return szekcioszin;
    }

    public void setSzekcioszin(Color szekcioszin) {
        this.szekcioszin = szekcioszin;
    }

    public Stroke getTeljesvonal() {
        return teljesvonal;
    }

    public void setTeljesvonal(Stroke teljesvonal) {
        this.teljesvonal = teljesvonal;
    }

    public Stroke getSzekciovonal() {
        return szekciovonal;
    }

    public void setSzekciovonal(Stroke szekciovonal) {
        this.szekciovonal = szekciovonal;
    }        
    
}
