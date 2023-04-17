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
public class Racstervezocsomopont {
    
    private int szekcio;
    private int kijelzes;
    Csomopont csomopont;

    public int getKijelzes() {
        return kijelzes;
    }

    public void setKijelzes(int kijelzes) {
        this.kijelzes = kijelzes;
    }
    
    public Racstervezocsomopont() {
    }

    public int getSzekcio() {
        return szekcio;
    }

    public void setSzekcio(int szekcio) {
        this.szekcio = szekcio;
    }

    public Csomopont getCsomopont() {
        return csomopont;
    }

    public void setCsomopont(Csomopont csomopont) {
        this.csomopont = csomopont;
    }
    
    
}
