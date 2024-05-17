def kripte_mo(mo):
    alfab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    kripte = []
    for karakte in mo:
        endeks = alfab.index(karakte.upper())
        kripte.append(str(endeks))
    return '-'.join(kripte)


mot_kripte = kripte_mo("ALlen")
print(mot_kripte)  
