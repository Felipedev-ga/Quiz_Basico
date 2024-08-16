import random
import string


def gerador_senha(len_pass = 8):
    ascii_opcoes = string.ascii_letters
    opc_numeros = string.digits
    punt_opcoes = string.punctuation
    
    opcao = ascii_opcoes + opc_numeros + punt_opcoes
    
    
    Senha_Usuario = '' 
    for i in range(0, len_pass):
        digito = random.choice(opcao)
        Senha_Usuario = Senha_Usuario + digito
        
        return Senha_Usuario
    
    
Digitos_Usuario = input('Quantos digitos na senha?')
    
if Digitos_Usuario.isdigit():
    Digitos_Usuario = int(Digitos_Usuario)