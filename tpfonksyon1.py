def an_miniskil(fraz):
    return fraz.lower()

def chenn_an_lis(chenn):
    return chenn.split()

def premye_let_chak_mo(fraz):
    return [mo[0] for mo in chenn_an_lis(an_miniskil(fraz))]

def ranplase_karakte(fraz, karakte_anvan, karakte_apre):
    return fraz.replace(karakte_anvan, karakte_apre)

def inverser_et_majiskil(chenn):
    chenn_invese = ''.join(reversed(chenn))  # Invese chèn an
    chenn_majiskil = chenn_invese.upper()  # Mete tout karaktè yo an majiskil
    return chenn_majiskil

# Test
fraz = "Ayibobo tou ayisyen anakonda"
print("An miniskil:", an_miniskil(fraz))
print("Chenn an lis:", chenn_an_lis(an_miniskil(fraz)))
print("Premye lèt chak mo:", premye_let_chak_mo(fraz))
print("Ranplase karaktè:", ranplase_karakte(fraz, "a", "@"))
print("envèse:",inverser_et_majiskil(fraz))
