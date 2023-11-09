from random import shuffle

ausentes = ["Tomas Lopez Croce", "Dahiana Portillo", "Julieta Popovich", "Rocío Yulan", "Luana Zalcman", "Agostina Gomez Borelli", "Gerónimo Solis", "Verónica Lagraña" ]
shuffle(ausentes)

print("\nGrupo 1:")
for i in ausentes[0:4]:
    indice = ausentes.index(i)
    print(f"{indice+1}- {i}")

print("\nGrupo 2:")
for i in ausentes[4:9]:
    indice = ausentes.index(i)
    print(f"{indice+1}- {i}")
print(" ")