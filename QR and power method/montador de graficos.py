import matplotlib.pyplot as plt


arq = open("dados", "r")
n = "primeiro"
erro = []
inv = []
simetrica = []
for i in arq:
    elem = i.split("&")
    erro.append(float(elem[2]))
    inv.append(float(elem[0]))
    simetrica.append(float(elem[1]))
plt.plot(erro,color = 'purple')
plt.plot(inv, color = 'red')
plt.plot(simetrica)
plt.show()