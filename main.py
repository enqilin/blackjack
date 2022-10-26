from random import choice,sample
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 
print("Punto de la carta {}".format(cartas.values()))
for carta, valor in cartas.items():
  print("La carta {} vale {}".format(carta,valor))
for carta in cartas.keys():
  print("La carta {} vale {}".format(carta, cartas[carta]))
lista=list(cartas)
print("Escoge una carta")
jugador=choice(lista)
punto_jugador=cartas[carta]
jugador=choice(lista)
punto_jugador+=cartas[carta]
print("La puntuación de la carta es: ",punto_jugador)
banca=sample(lista,2)
punto_banca=sum(cartas[carta] for carta in banca)
print("Las cartas ecogida {} {}, y su puntuación es: {}".format(banca[0],banca[1],punto_banca))

