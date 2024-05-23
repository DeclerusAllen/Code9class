non=input("antre non w silvouplè: ")

def nan_foma(non):
    mo=non.split()
    mo_tit=[m.capitalize() for m in mo]
    non_tit=" ".join(mo_tit)
    return non_tit

nouvo_non=nan_foma(non)
print(nouvo_non)
