''' 
    TODO Leia as as entradas e crie as condições necessárias para verificar se é maior ou
    menor do que 8000 e imprima "Inseto!" ou "Maior que 8000!" para cada caso.
'''

C = int(input()) 
for i in range(C):
  
  N = int(input())

  if N <= 8000:
    print('Inseto!')
  else:
    print('Mais de 8000!')

