/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Entities;

import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author sd-leap
 */
public class Szelvenyelemek {
    
    Float ex,ey;                                   // A rajzon a súlypont távolsága balról és fentről  
    Integer maxx,maxy;                             // A képen lévő rajzolt szelvény maximális mérete 100*-os nagyításban 
    Color rajzszin;                                      // Az alkotó szelvény kijelzett színe
    Integer poziciox,pozicioy;                           // A teljes rajzon a szelvény koordinátája
    List<Konturvonal> konturvonal= new ArrayList<>();   // A kontúrvonalak X-,Y- koordinátái 100*-os nagyításban 
    
    public Float getEx() {
        return ex;
    }

    public void setEx(Float ex) {
        this.ex = ex;
    }

    public Float getEy() {
        return ey;
    }

    public void setEy(Float ey) {
        this.ey = ey;
    }

    public Color getRajzszin() {
        return rajzszin;
    }

    public void setRajzszin(Color rajzszin) {
        this.rajzszin = rajzszin;
    }

    public Integer getMaxmeret() {
        return 2000;
    }

    public Integer getMaxx() {
        return maxx;
    }

    public void setMaxx(Integer maxx) {
        this.maxx = maxx;
    }

    public Integer getMaxy() {
        return maxy;
    }

    public void setMaxy(Integer maxy) {
        this.maxy = maxy;
    }

    public Integer getPoziciox() {
        return poziciox;
    }

    public void setPoziciox(Integer poziciox) {
        this.poziciox = poziciox;
    }

    public Integer getPozicioy() {
        return pozicioy;
    }

    public void setPozicioy(Integer pozicioy) {
        this.pozicioy = pozicioy;
    }

    public List<Konturvonal> getKonturvonal() {
        return konturvonal;
    }

    public void setKonturvonal(List<Konturvonal> konturvonal) {
        this.konturvonal = konturvonal;
    }


    
    
}
