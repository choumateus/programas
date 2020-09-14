import random
nome = ["Mateus", "Marcos", "Lucas", "João" ,"Pedro"]
nome2 = ["Ana", "Kelly", "Julia", "Raquel", "Maria"]
sexo = "MF"
N = "joao"
print("insert invencao values")
for i in range( 10000):
    S=sexo[random.randint(0,1)]
    if S == "M":
        N = nome[random.randint(0,4)]
    if S == "F":
        N = nome2[random.randint(0,4)]
    if i <9999:
        print('('+'"'+N+'"'+', '+str(random.randint(0,40))+', "'+S + '"'+ ")"+ ',')
    if i == 9999:
        print('('+'"'+N+'"'+', '+str(random.randint(0,40))+', "'+S + '"'+ ")"+ ';')
