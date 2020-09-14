from random import seed, randrange
#Importando oque o enunciado do EP deu

#As duas funções do enunciado do EP em só uma(gerar e imprimir a amostra)
def gera_e_imprime(a,b,n):
        #Numero USP como semente
        NUSP = 11221352
        seed(NUSP)
        amostra = n * [0]
        print("   AMOSTRA:")
        for k in range(n):
                #Gerando a amostra
                amostra[k] = a + float(randrange(1000000)) * (b - a)/1000000.0
                #Imprimindo 5 numeros por linha
                if k % 5 == 4: print("%10.5f" %amostra[k])
                else: print("%10.5f" %amostra[k], end = ' ')
        print()
        return amostra

#Função que divide a amostra em n intervalos e também monta o histograma
#Função que rinicia o programa se for inserido um numero menos ou igual a 0
def divide_e_monta(intervalo,amostra):
        while True:
                print()
                #entrada da quantidade de intervalos pra montar o histograma
                print("se você inserir um valor negativo ou nulo, o programa reinicia!")
                n_inters = int(input("Entre com a quantidade de intervalos que você quer dividir a amostra(valor inteiro, positivo e numérico): "))
                # reinicia se o usuário inserir o numero 0
                if n_inters <= 0:
                    print("\n", 5* " *", "Ao inserir uma quantidade nula ou negativa, você reinicia o programa :)", 5 * "* ", "\n")
                    break
        #botando um limite de 0,001 de um intervalo para outro
                valor = ((intervalo[1]-intervalo[0])/n_inters)
                limite = (intervalo[1]-intervalo[0])*1000
                if valor < 0.001:
                        print("\n",5*"* ","Com este valor, a diferença entre dois intervalos seguidos é menor que 0,001, é necessário fornecer um valor até", limite, "para não ser menos que isso", "\n",5*" *")
                        break
                else:
        #faz uma lista com as divisoes que a amostra sera separada
                        divisoes = [[0,0] for i in range(n_inters)]
                        for k in range(n_inters):
                                divisoes[k][0] = intervalo[0] + valor*k
                                divisoes[k][1] = intervalo[0] + valor*(k+1)
        #cria uma lista no qual os elementos sao as listas divididas
                        lista = [[] for k in range(n_inters)]
                        for elemento in amostra:
                                for k in range(len(divisoes)):
                                        if elemento >= divisoes[k][0] and elemento < divisoes[k][1]:
                                                lista[k].append(elemento)
        #frequencia é uma lista com a quantidade de elementos presentes na "sublista" criada anteriormente
                        frequencia = [len(lista[k]) for k in range(len(lista))]
                        mx = max(frequencia)
        #grafico é uma lista feita a partir de frequencia, criada para obtermos um valor proporcional, para o desenho do histograma
                        grafico = [round(70 * frequencia[k] / mx) for k in range(len(frequencia))]
        #mostra o histograma sendo "divisoes" o intervalo de k e k+1, "freq" como frequencia e "freq_graf" como a quantidade de barras
                        print("{}Intervalo{}Frequência{}Gráfico".format(6*" ",10*" ",5*" "))
                        for k  in range(len(divisoes)):
                                print("{a}{intervalo1}  A {intervalo2}{b}{frequencia}{c}{grafico}".format(a = 2*" ", intervalo1 = "%6.3f" %divisoes[k][0],intervalo2 = "%6.3f" %divisoes[k][1],b = 10*" ",frequencia = "%3i" %frequencia[k],c = 9*" ",grafico = grafico[k]*"\u2593"))

#função que vai rodar as funções e o programa em geral
def rodar():
        while True:
                print("\n",5*"* ","Início do Histograma",5*" *","\n")
                #entrando com os intervalos
                primeirointer = float(input("entre com o primeiro valor do intervalo(valor numérico): "))
                segundointer = float(input("entre com o segundo valor do intervalo(valor numérico): "))
                # caso o usuario entre com o msm numero no primeiro e no segundo valor do intervalo
                while primeirointer >= segundointer:  #mesmos comandos de cima, dentro do while, para não serem inseridos dois intervalos iguais
                    print("\n", 5 * "* ", "O primeiro valor do intervalo deve ser maior que o segundo", 5 * " *",
                          "\n")
                    primeirointer = float(input("entre com o primeiro valor do intervalo(valor numérico): "))
                    segundointer = float(input("entre com o segundo valor do intervalo(valor numérico): "))
                # entrando com a quantidade de elementos na amostra que precisa ser maior que 0 e inteiro
                quantidade = int(input("Entre com a quantidade de elementos da amostra(valor positivo, inteiro e numérico): "))
                while quantidade <=0:
                    print("a quantidade da amostra precisa ser maior que 0")
                    quantidade = int(input("Entre com a quantidade de elementos da amostra(valor positivo, inteiro e numérico): "))
                #gerando a amostra
                AMOSTRA = gera_e_imprime(primeirointer,segundointer,quantidade)
                INTERVALO = [primeirointer,segundointer]
                #gerador em loop do grafico
                FIM = divide_e_monta(INTERVALO,AMOSTRA)
#inicio do programa
rodar()

