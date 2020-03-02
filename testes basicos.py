fila=[0,1,2,3,4]
a=0
for i in range(5):
    if  fila[i]==2 or fila[i] == 3:
        print("oi")
        fila[i],fila[a] = fila[a], fila[i]
        a+=1
        print(fila)
print(fila)
