#Crie um programa que leia os numeros e imprima o menor e o menor valor

def maxOrmin(*args):
 lista =list(args)
 maiorNumero = max(lista)
 menorNumero = min(lista)
 print(f"A maior numero é: {maiorNumero}")
 print(f"A menor numero é: {menorNumero}")

maxOrmin(22,45,13,996,14,558) 