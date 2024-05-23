import os

class GestionFichye:
    def __init__(self, chemen_fichye):
        self.chemen_fichye = chemen_fichye

    def li(self):
        with open(self.chemen_fichye, 'r') as fichier:
            kontni = fichier.read()
        return kontni

    def ajoute(self, texte):
        with open(self.chemen_fichye, 'a') as fichier:
            fichier.write(texte)

    def efase_kontni(self):
        with open(self.chemen_fichye, 'w') as fichier:
            fichier.truncate(0)

    def efase_fichye(self):
        try:
            os.remove(self.chemen_fichye)
            print("Fichye a efase avèk siksè.")
        except FileNotFoundError:
            print("Fichye a pa egziste.")
        except PermissionError:
            print("Ou pa gen pèmisyon pou efase fichye a.")

fichye = "al.txt"


gestion_fichye = GestionFichye(fichye)
print("Kontni a: ", gestion_fichye.li())

gestion_fichye.ajoute("Nouvo kontni.")
print("Kontni a apre ajoute: ", gestion_fichye.li())

gestion_fichye.efase_kontni()
print("Kontni a apre efase: ", gestion_fichye.li())

gestion_fichye.efase_fichye()
