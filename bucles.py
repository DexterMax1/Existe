lista = ["Mujer", "Hombre", "10", "Hola", "9", "Sapo"]

print(lista)

for iterar in lista:
    print(iterar)
    if iterar == "Hola": 
        print("La palabra si existe")
        break
    else:
        print("La palabra no existe")
    