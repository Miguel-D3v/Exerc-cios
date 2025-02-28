""" Crie um programa que determine se uma pessoa é maior de idade. """

age = int(input("Digite a idade: "))

def checkAge(age):
 if(age < 18):
  return "Essa pessoa é menor de idade"
 else:
  return "Essa pessoa é maior de idade"


print(checkAge(age))
