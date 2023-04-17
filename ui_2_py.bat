del *.bak

rem ren statika.py statika.bak
ren drotvaz.py drotvaz.bak
ren kmjellossz.py kmjellossz.bak
ren kocka.py kocka.bak
rem ren tartok.py tartok.bak
ren racstervezo.py racstervezo.bak
ren projekt.py projekt.bak
ren kettamaszu.py kettamaszu.bak
ren kmjell.py kmjell.bak

rem pyuic5 -x statika.ui -o statika.py
pyuic5 -x drotvaz.ui -o drotvaz.py
pyuic5 -x kmjellossz.ui -o kmjellossz.py
pyuic5 -x kocka.ui -o kocka.py
rem pyuic5 -x tartok.ui -o tartok.py
pyuic5 -x racstervezo.ui -o racstervezo.py
pyuic5 -x projekt.ui -o projekt.py
pyuic5 -x kettamaszu.ui -o kettamaszu.py
pyuic5 -x kmjell.ui -o kmjell.py
