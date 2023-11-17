from tkinter import Frame

import random


def sulyozott_veletlen_kivalasztas(lista, sulyok):
    # Ellenőrzés, hogy a súlyok száma egyezik-e a lista elemeinek számával
    if len(lista) != len(sulyok):
        raise ValueError("A lista és a súlyok hossza nem egyezik meg.")

    # Súlyozott véletlenszerű kiválasztás
    valasztott_elem = random.choices(lista, weights=sulyok, k=1)[0]

    return valasztott_elem


# Példa
elemek = ['A', 'B', 'C', 'D']
sulyok = [0.1, 0.3, 0.4, 100]

fut = 1000

lista = []
for i in range(fut):
    valasztott = sulyozott_veletlen_kivalasztas(elemek, sulyok)
    lista.append(valasztott)
print(lista)
print("Súlyozott véletlenszerűen kiválasztott elem:", valasztott)

a,b,c,d = 0,0,0,0

for i in lista:
    if i == 'A':
        a += 1
    if i == 'B':
        b += 1
    if i == 'C':
        c += 1
    if i == 'D':
        d += 1

print (a,b,c,d)


