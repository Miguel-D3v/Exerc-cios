"""
  Escreva um programa que calcule o IMC de uma pessoa.
 """

def imc(peso,altura):
  calc = peso/(altura*altura)
  calc = round(calc,2)

  if(calc < 18.5):
    return "Abaixo do peso"
  if(calc > 18.5 and calc < 24.9):
    return "Peso normal"
  if(calc > 25 and calc < 29.9):
    return  "Sobrepeso"
  if(calc > 30):
    return "Obesidade"

print(imc(85,1.70))
