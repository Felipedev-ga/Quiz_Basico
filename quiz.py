print('Seja bem-vindo ao Quiz sobre Ciência de Dados!')

iniOUn = input('Deseja começar (S/N)?\n')

if iniOUn.lower() != 's':
    print('Volte quando desejar jogar.')
    quit()

ponto = 0
    

print('\nPergunta 1: O que é Ciência de Dados?')
print('(A) Estudo de como organizar grandes volumes de dados.')
print('(B) Análise estatística de dados.')
print('(C) Processo de extrair conhecimento e insights a partir de dados.')
print('(D) Programação para análise de dados.')

re1 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re1.upper() == 'C':
    print('Resposta correta! Ciência de Dados é o processo de extrair conhecimento e insights a partir de dados.')
    ponto += 1 
else:
    print('Resposta incorreta! Ciência de Dados é: C) Processo de extrair conhecimento e insights a partir de dados.')


print('\nPergunta 2: Qual é o primeiro passo do processo de Ciência de Dados?')
print('(A) Coleta de dados.')
print('(B) Análise de dados.')
print('(C) Comunicação dos resultados.')
print('(D) Modelagem de dados.')

re2 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re2.upper() == 'A':
    print('Resposta correta! O primeiro passo da Ciência de Dados é a coleta de dados.')
    ponto += 1 
else:
    print('Resposta incorreta! O primeiro passo do processo de Ciência de Dados é: A) Coleta de dados.')


print('\nPergunta 3: O que é Machine Learning?')
print('(A) Técnica para construir máquinas virtuais.')
print('(B) Processo de ensinar máquinas a aprender com dados.')
print('(C) Análise estatística de dados.')
print('(D) Técnica para compressão de dados.')

re3 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re3.upper() == 'B':
    print('Resposta correta! Machine Learning é o processo de ensinar máquinas a aprender com dados.')
    ponto += 1 
else:
    print('Resposta incorreta! Machine Learning é: B) Processo de ensinar máquinas a aprender com dados.')


print('\nPergunta 4: Qual é a principal linguagem de programação usada em Ciência de Dados?')
print('(A) Java.')
print('(B) C++.')
print('(C) Python.')
print('(D) Ruby.')

re4 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re4.upper() == 'C':
    print('Resposta correta! Python é a linguagem de programação mais usada em Ciência de Dados.')
    ponto += 1 
else:
    print('Resposta incorreta! A principal linguagem de programação usada em Ciência de Dados é: C) Python.')


print('\nPergunta 5: O que é Big Data?')
print('(A) Conjunto de técnicas para análise de dados.')
print('(B) Conjunto de dados pequenos.')
print('(C) Termo para grandes volumes de dados.')
print('(D) Ferramenta de visualização de dados.')

re5 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re5.upper() == 'C':
    print('Resposta correta! Big Data se refere a grandes volumes de dados.')
    ponto += 1 
else:
    print('Resposta incorreta! Big Data é: C) Termo para grandes volumes de dados.')

print('\nPergunta 6: Qual é o objetivo da Análise Exploratória de Dados?')
print('(A) Prever o futuro com precisão.')
print('(B) Limpar dados inconsistentes.')
print('(C) Resumir dados para visualização.')
print('(D) Comunicar resultados para o público.')

re6 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re6.upper() == 'C':
    print('Resposta correta! A Análise Exploratória de Dados visa resumir dados para visualização.')
    ponto += 1 
else:
    print('Resposta incorreta! O objetivo da Análise Exploratória de Dados é: C) Resumir dados para visualização.')

print('\nPergunta 7: Qual é a finalidade da Visualização de Dados?')
print('(A) Transformar dados em informações acionáveis.')
print('(B) Reduzir a precisão dos dados.')
print('(C) Aumentar o tamanho dos dados.')
print('(D) Acelerar a coleta de dados.')

re7 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re7.upper() == 'A':
    print('Resposta correta! Visualização de Dados transforma dados em informações acionáveis.')
    ponto += 1 
else:
    print('Resposta incorreta! A finalidade da Visualização de Dados é: A) Transformar dados em informações acionáveis.')


print('\nPergunta 8: O que é um algoritmo em Ciência de Dados?')
print('(A) Um conjunto de regras para desenho gráfico.')
print('(B) Um método matemático para resolver problemas.')
print('(C) Um programa de computador sem utilidade prática.')
print('(D) Uma imagem digital de um processo.')

re8 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re8.upper() == 'B':
    print('Resposta correta! Um algoritmo em Ciência de Dados é um método matemático para resolver problemas.')
    ponto += 1 
else:
    print('Resposta incorreta! Um algoritmo em Ciência de Dados é: B) Um método matemático para resolver problemas.')

print('\nPergunta 9: O que significa "Data Cleaning" em Ciência de Dados?')
print('(A) Limpeza de dados sujos.')
print('(B) Guardar dados em um arquivo.')
print('(C) Aumentar o tamanho dos dados.')
print('(D) Transformar dados em informações.')

re9 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re9.upper() == 'A':
    print('Resposta correta! "Data Cleaning" refere-se à limpeza de dados sujos ou inconsistentes.')
    ponto += 1 
else:
    print('Resposta incorreta! "Data Cleaning" em Ciência de Dados é: A) Limpeza de dados sujos.')


print('\nPergunta 10: Qual é o papel de um Cientista de Dados?')
print('(A) Construir websites interativos.')
print('(B) Analisar dados para extrair insights.')
print('(C) Projetar redes de computadores.')
print('(D) Escrever roteiros para filmes.')

re10 = input('Qual é a sua resposta (A/B/C/D)?\n')
if re10.upper() == 'B':
    print('Resposta correta! O papel de um Cientista de Dados é analisar dados para extrair insights.')
    ponto += 1 
else:
    print('Resposta incorreta! O papel de um Cientista de Dados é: B) Analisar dados para extrair insights.')

print(f'\nObrigado por participar do Quiz! Sua pontuação final é de {ponto} pontos.')
