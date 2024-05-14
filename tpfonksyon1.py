def an_miniskil(chenn):
    return fraz.lower()

def chenn_an_lis(chenn):
    return chenn.split()

def premye_let_chak_mo(chenn):
    return [mo[0] for mo in chenn_an_lis(an_miniskil(fraz))]

def ranplase_karakte(fraz, karakte_anvan, karakte_apre):
    return fraz.replace(karakte_anvan, karakte_apre)

def inverser_et_majiskil(chenn):
    chenn_invese = ''.join(reversed(chenn))  # Invese chèn an
    chenn_majiskil = chenn_invese.upper()  # Mete tout karaktè yo an majiskil
    return chenn_majiskil
def trouve(chenn):
    return chenn.find("a")

def total_endeks(chenn):
    total=0
    for i, karaktè in enumerate(chenn):
        if karaktè.lower()=="a":
            total +=i
    return total
# Test
fraz = "Ayibobo tou ayisyen anakonda"
print("1) An miniskil:", an_miniskil(fraz))
print("")
print("2) Chenn an lis:", chenn_an_lis(an_miniskil(fraz)))
print("")
print("3) Premye lèt chak mo:", premye_let_chak_mo(fraz))
print("")
print("4) Ranplase karaktè:", ranplase_karakte(fraz, "a", "@"))
print("")
print("5) envès:",inverser_et_majiskil(fraz))
print("")
print("6) premye endèks a:",trouve(fraz))
print("")
print("7) total endèks 'a':",total_endeks(fraz))
print("")