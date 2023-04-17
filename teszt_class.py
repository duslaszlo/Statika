from entities.szelveny import Szelveny
from entities.rud import Rud
import time
sz = Szelveny(100, 'neve', 'filenev1231231', 100, 200, 1, 2, 3, 4, 5, 61, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 3, 4, 5, 6, 7, 7, 2, 3, 4, 3, 34)
print (sz.filenev)

#def __init__(self, id, projekt, azonosito, kezdocsp, vegecsp, anyag, piros, zold, kek, vastagsag, szelveny, mark)
r: Rud = Rud(1, 'projekt', 'azonosito', 1, 2, 'Anyag', 0, 0, 0, 0,'szelveny',0)

print (r.azonosito)