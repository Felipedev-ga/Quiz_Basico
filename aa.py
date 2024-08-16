import random as rd

classe_personagem = []
herois = [
    "Goku",
    "Vegeta",
    "Gohan",
    "Piccolo",
    "Trunks",
    "Krillin",
    "Yamcha",
    "Tien Shinhan",
    "Android 18",
    "Master Roshi"
]

viloes = [
    "Frieza",
    "Cell",
    "Majin Buu",
    "Broly",
    "Raditz",
    "Nappa",
    "Captain Ginyu",
    "Zarbon",
    "Dodoria",
    "Dr. Gero"
]
while True:
    print('Seja bem vindo ao jogo de rpg')
    print('Irei sortear qual classe você sera, heroi ou vilão')
    
    escolha = int(input('Escolha um número aleatorio de 0 a 10'))
    Vil_her = rd.randint(0,9)
    
    if escolha == Vil_her:
        classe_personagem = herois
        my_heroi = herois