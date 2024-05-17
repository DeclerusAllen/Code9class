def an_miniskil(chenn):
    return fraz.lower()

def chenn_an_lis(chenn):
    return chenn.split()

def premye_let_chak_mo(chenn):
    return [mo[0] for mo in chenn_an_lis(an_miniskil(chenn))]

def an_maj(chenn):
    return chenn.title()

def ranplase_karakte(fraz, karakte_anvan, karakte_apre):
    return fraz.replace(karakte_anvan, karakte_apre)

def inverser_et_majiskil(chenn):
    chenn_invese = (''.join(reversed(chenn))).upper()  
    return chenn_invese
def trouve(chenn):
    return chenn.find("a")

def total_endeks(chenn):
    total=0
    for i, karaktè in enumerate(chenn):
        if karaktè.lower()=="a":
            total +=i
    return total

def endeks_lis(chenn):
    return [i for i, karakte in enumerate(chenn) if karakte == "a"]

def retire_espas_et_concatene(chenn):
    chenn_sans_espas = chenn.replace(" ", "")
    rezilta = chenn_sans_espas + str(len(chenn_sans_espas))
    return rezilta

# Test
fraz = "Ayibobo tou ayisyen anakonda"
print("1) An miniskil:", an_miniskil(fraz))
print("")
print("2) Chenn an lis:", chenn_an_lis(an_miniskil(fraz)))
print("")
print("3) premye lèt an majiskil:",an_maj(fraz))
print("4) Premye lèt chak mo:", premye_let_chak_mo(fraz))
print("")
print("5) Ranplase karaktè:", ranplase_karakte(fraz, "a", "@"))
print("")
print("6) envès:",inverser_et_majiskil(fraz))
print("")
print("7) premye endèks a:",trouve(fraz))
print("")
print("8) total endèks 'a':",total_endeks(fraz))
print("")
print("9) endeks lis:", endeks_lis(fraz))
print("")
print("10) nouvo lis la ak kantite karaktè a:", retire_espas_et_concatene(fraz))