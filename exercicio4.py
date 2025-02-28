"""
 Faça um programa que verifique se um número é par ou ímpar.
 """

number = int(input("Digite um numero: "))

def checkNumber(number):
  if(number % 2 == 0):
   return "Esse numero é par"
  else:
   return "Esse numero é impar"

print(checkNumber(number))
