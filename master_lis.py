def kreye_lis_divizib_pa_de(n):
    return [i for i in range(n+1) if i % 2 == 0]

def konveti_an_chenn(liste_entye):
    return list(map(str, liste_entye))

def konveti_miniskil_an_majiskil(liste_chenn_miniskil):
    return [mois.upper() for mois in liste_chenn_miniskil]

def kreye_nouvo_lis_divizib_pa_twa(lis_orijinal):
    return [lis_orijinal[i:i+3] for i in range(0, len(lis_orijinal), 3)]

def kreye_nouvo_lis_gwoupe_tipl(lis_orijinal):
    return [(lis_orijinal[i], lis_orijinal[i+1], lis_orijinal[i+2]) for i in range(0, len(lis_orijinal), 3)]

def konveti_sans_doublon(lis_avek_doublon):
    return list(set(lis_avek_doublon))

def kreye_nouvo_lis_komen(lis1, lis2):
    return list(set(lis1) & set(lis2))

def kreye_nouvo_lis_distenge(lis1, lis2):
    return list(set(lis1) ^ set(lis2))

def kreye_lis_kle_valè(diksyone):
    return list(diksyone.keys()), list(diksyone.values())

def reyini_twa_lis(lis1, lis2, lis3):
    return list(set(lis1 + lis2 + lis3))

#test
print("")
print("1) lis antye divizib pa 2 a se:", kreye_lis_divizib_pa_de(100))
print("")
print("1) lis antye divizib pa 2 a se:", kreye_lis_divizib_pa_de(100))

print("")
print("2) konveti lis antye an chenn:", konveti_an_chenn([1, 2, 3, 4, 5]))

print("")
print("3) konveti lis miniskil an majiskil:", konveti_miniskil_an_majiskil(['janvye', 'fevriye', 'mas']))

print("")
print("4) kreye nouvo lis divizib pa twa:", kreye_nouvo_lis_divizib_pa_twa([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print("")
print("5) kreye nouvo lis gwoupe tipl:", kreye_nouvo_lis_gwoupe_tipl([1, 2, 3, 4, 5, 6, 7, 8, 9,0]))

print("")
print("6) konveti lis avèk doublon:", konveti_sans_doublon([1, 2, 2, 3, 4, 4, 5]))

print("")
print("7) kreye nouvo lis komen:", kreye_nouvo_lis_komen([1, 2, 3], [3, 4, 5]))

print("")
print("8) kreye nouvo lis distenge:", kreye_nouvo_lis_distenge([1, 2, 3], [3, 4, 5]))
print("")
print("9) kreye lis kle valè:", kreye_lis_kle_valè({'a': 1, 'b': 2, 'c': 3}))

print("")
print("10) reyini twa lis:", reyini_twa_lis([1, 2], [2, 3], [3, 4]))

