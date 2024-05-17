def pran_valè(dic):
    values = [dic[key] for key in dic]
    return values

diksyone = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

#tes1
valè_yo =pran_valè(diksyone)
print(valè_yo)  

def verifye_parantèz(value):
    if value.startswith('{') and value.endswith('}'):
        return value
    else:
        return None


valè_itilizatè = input("Tanpri tape yon valè: ")

rezilta = verifye_parantèz(valè_itilizatè)

if rezilta:
    print(f"Valè a gen akolad devan ak dèyè: {rezilta}")
else:
    print("Valè a pa gen akolad devan ak dèyè.")

print("")
def afiche_kle(dic):
    for key in dic:
        print(key)


afiche_kle(diksyone)
print("")
def afiche_vale(dic):
    for value in dic.values():
        print(value)


afiche_vale(diksyone)
print("")
copy_dict = {key: value for key, value in diksyone.items()}
print(copy_dict)
