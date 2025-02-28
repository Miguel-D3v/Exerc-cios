#Faça um programa que inverta um vetor.

def invertVetor(vetor):
   vetor.reverse()
   return vetor


vetor=[2,5,45,77,2,0]
print(f"Vetor original , {vetor}")
invertingVetor=invertVetor(vetor)
print(f"Vetor invertido , {invertingVetor}")
