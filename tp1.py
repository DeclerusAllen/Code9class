fraz="Ayibobo tou ayisyen anakonda"

#an miniskil
miniskil=fraz.lower()
print(miniskil)

#chèn de karaktè an lis
name=miniskil.split()
print(name)

#premye lèt de chak mo
tit=fraz.title()
print(tit)

#rekipere premye lèt nan chak mo
premye_let = [mo[0] for mo in name] 
print(premye_let )

#ranplase karaktè
fraz_mod=fraz.replace("a","@")
print(fraz_mod)

