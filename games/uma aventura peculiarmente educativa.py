import time
import random
#definicao de funcoes
def mostra_atributos(nome,idade,classe,inteligencia,forca,game_over):
    if game_over == -1:
        return
    print("-----Atributos-----")
    print("nome:",nome)
    print("idade:", idade)
    print("classe:", classe)
    print("inteligencia:", (inteligencia*10)*"\u2588")
    print("forca:       ",(forca*10)*"\u2588")
    print("-------------------")
def fase_xandao(tempo,personagens,perdidos,nome,forca):
    random.shuffle(personagens)
    personagem = personagens[2]
    print("Oh nao....")
    time.sleep(2)
    print("Xandao da digitacao apareceu!")
    time.sleep(2)
    print("Ele pegou "+ personagem + "!!")
    time.sleep(1)
    print("Xandao: HA HA HA!")
    time.sleep(1)
    print("Xandao: Se voce quiser levar", personagem, "de volta, vai ter que me vencer em um duelo de digitacao! Você aceita o desafio?(S/N)")
    R = str(input())
    if R == "N":
        perdidos.append(personagem)
        personagens.pop(personagens.index(personagem))
        print(personagem+": porque...?")
        time.sleep(1)
        print("Xandao: ARREGÃO! Agora vai embora e segue seu caminho!")
        time.sleep(1)
        return 0
    if R == "S":
        frases = ["nescau>toddy","amanha vou no clube","agua coca latao","messi>CR7","brtt>doublelift"
                  ,"black lives matter","setembro amarelo","pai ta on", "EA sports","Matematica é 10"]
        random.shuffle(frases)
        personagens.pop(personagens.index(personagem))
        print("Xandao: Ótimo! Vamos para o duelo!")
        print("Xandao: As regras são claras, vão aparecer no terminal algumas frases, ")
        print("Xandao: você tem que redigitar essas frases mais rapido que eu.")
        input("(aperte enter pra continuar)")
        print("Xandao: caso você perca por mais de 10 segundos, eu te mato")
        print("Xandao: caso voce perca por menos de 10 segundos eu fico com", personagem, "e voce segue seu caminho")
        input("(aperte enter para continuar)")
        print(nome+": Beleza! bora pro duelo!")
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("VALENDO!")
        usuario = "nada"
        tempo1 = time.time()
        for i in frases:
            while usuario != i:
                print(i)
                usuario = str(input())
        tempo_demorado = time.time() - tempo1
        tempo_possivel = tempo+forca*5
        if tempo_possivel - (tempo_demorado)>0:
            print("Xandao: Droga...")
            time.sleep(1)
            print("Xandao: Voce me derrotou, naaaaoooo!")
            time.sleep(1)
            print("Xandao: pode levar", personagem, "e ir embora")
            time.sleep(1)
            return 2
        elif tempo_possivel - tempo_demorado <-10:
            print("Xandao: HA HA SEU LOSER!")
            time.sleep(1)
            print("Xandao: VOU ACABAR COM VOCE!")
            time.sleep(1)
            return -1
        else:
            perdidos.append(personagem)
            print("Xandao: Bom, eu ganhei, mas foi por muito pouco")
            time.sleep(1)
            print("Xandao:",personagem,"vai ficar cmg, ja voce, xispa! siga sua jornada!")
            time.sleep(1)
            return 1
def fase_newton(personagens,perdidos,nome,inteligencia,media,game_over):
    if game_over == -1:
        return
    random.shuffle(personagens)
    personagem = personagens[1]
    print("Seguindo a trilha, ocorre algo inesperado...")
    time.sleep(2)
    print("ISAAC MONSTREWTON! O genio capturou "+ personagem + "!!")
    time.sleep(1)
    print("Isaac: E=mc^2! Quero fazer",personagem,"de cobaia!")
    time.sleep(1)
    print("Isaac: Se voce quiser levar", personagem,
          "de volta, vai ter que responder um questionario academico! Você aceita o desafio?(S/N)")
    R = str(input())
    if R == "N":
        perdidos.append(personagem)
        personagens.pop(personagens.index(personagem))
        print(personagem+": porque...?")
        time.sleep(1)
        print("Isaac: Beleza! vou fazer varios experimentos hehe...")
        time.sleep(1)
        print("Isaac: Agora vai embora e segue seu caminho!")
        time.sleep(1)
        return 0
    if R == "S":
        questoes_fase2 = [["qual a formula da agua?", "H2O"], ["quem descobriu o Brasil (só primeiro nome)", "Pedro"],
                          ["3 x 42 = ?", "126"],
                          ["escreva um codigo em javascript no qual mostra no terminal 'Hello World'",
                           "console.log('Hello World')"],
                          ["formula basica da forca?(tudo em maiusculo)", "F=MA"],
                          ["qual organela é responsável pela respiração?", "mitocondria"],
                          ["Qual a Capital do Espirito Santo?", "Vitoria"],
                          ["Escreva o numero de pi com apenas duas casas decimais", "3,14"],
                          ["Qual o apelido do maior tenista brasileiro da historia?", "Guga"],
                          ["Qual empresa que o Bill Gates criou?", "Microsoft"]]
        random.shuffle(questoes_fase2)
        numero_passar=round((10)*(media-0.2)) - inteligencia
        numero_ganhar=round((10)*media) - inteligencia
        personagens.pop(personagens.index(personagem))
        print("Isaac: Ótimo! Vamos para o questionario!")
        print("Isaac: As regras são as seguintes, vão aparecer no terminal algumas perguntas, ")
        print("Isaac: você tem que responder corretamente essas perguntas.")
        input("(aperte enter pra continuar)")
        print("Isaac: caso você acerte menos que", numero_passar,"questoes, eu arranco seu cerebro")
        print("Isaac: caso voce acerte menos que",numero_ganhar,"questoes, eu levo", personagem, "e voce segue seu caminho")
        print("Isaac: Você tem no maximo 3 tentativas para acertar cada questao!")
        input("(aperte enter para continuar)")
        print(nome+": Beleza! bora pro quiz!")
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("VALENDO!")
        usuario = "nada"
        contador_de_acertos = 0
        for i in questoes_fase2:
            tentativas = 0
            while usuario != i[1] and tentativas<3:
                print(i[0])
                usuario = str(input("Resposta:"))
                tentativas+=1
            if tentativas <3:
                contador_de_acertos+=1
        if contador_de_acertos >= numero_ganhar:
            print("Isaac: Nao acredito...")
            time.sleep(1)
            print("Isaac: Voce é um genio!")
            time.sleep(1)
            print("Isaac: pode levar", personagem, "e ir embora")
            time.sleep(1)
            return 2
        elif contador_de_acertos <numero_passar:
            print("Isaac: HA HA VOCE NAO PASSOU!")
            time.sleep(1)
            print("Isaac: SEU CEREBRO É MEU!")
            time.sleep(1)
            return -1
        else:
            perdidos.append(personagem)
            print("Isaac: Bom, como voce nao passou por pouco")
            time.sleep(1)
            print("Isaac:",personagem,"vai ficar cmg, mas voce pode seguir sua jornada!")
            time.sleep(1)
            return 1
def fase_final(personagens,perdidos,nome,inteligencia,forca,media,game_over,tempo_final):
    if game_over == -1:
        return
    personagem = personagens[0]
    print("Ja chegando em sua tribo, alguem assustador surge...")
    time.sleep(2)
    print("L UCHIHA! O mestre raptou "+ personagem + "!!")
    time.sleep(1)
    print("L UCHIHA: soube que voce derrotou meus pupilos! por isso vou me vingar deles raptando",personagem)
    time.sleep(1)
    print("L UCHIHA: Se voce quiser levar", personagem,
          "de volta, vai ter que responder um questionario com limite de tempo! Você aceita o desafio?(S/N)")
    R = str(input())
    if R == "N":
        perdidos.append(personagem)
        personagens.pop(personagens.index(personagem))
        print(personagem+": porque...?")
        time.sleep(1)
        print("L UCHIHA: Beleza! vou fazer varios experimentos hehe...")
        time.sleep(1)
        print("L UCHIHA: Agora vai embora e segue seu caminho!")
        time.sleep(1)
        return 0
    if R == "S":
        questoes_fase_final = [["qual a formula do ácido clorídrico?", "HCl"], ["quem é o principal ícone da segunda guerra mundial?", "Hitler"],
                          [" 16^3 = ?", "4096"],
                          ["crie uma lista chamada numeros em python com formato (2;5;7)",
                           "numeros = [2,5,7]"],
                          ["formula basica da velocidade?(tudo em maiusculo, use V para velocidade, D para distancia e T para tempo)", "V=D/T"],
                          ["complete o nome da organela, Complexo de ______", "Golgi"],
                          ["Qual a Capital do Peru?", "Lima"],
                          ["Escreva o valor da gravidade da Terra em m/s^2 com apenas uma casa decimal", "9,8"],
                          ["Qual o apelido do maior futebolista brasileiro da historia?", "Pele"],
                          ["Qual empresa que o Steve Jobs criou?", "Apple"]]
        random.shuffle(questoes_fase_final)
        numero_passar=round((10)*(media-0.2)) - inteligencia
        numero_ganhar=round((10)*media) - inteligencia
        personagens.pop(personagens.index(personagem))
        print("L UCHIHA: Ótimo! Vamos para o questionario!")
        print("L UCHIHA: As regras são as seguintes, vão aparecer no terminal algumas perguntas, ")
        print("L UCHIHA: você tem que responder corretamente essas perguntas e com um tempo limitado.")
        input("(aperte enter pra continuar)")
        print("L UCHIHA: caso você acerte menos que", numero_passar," questoes ou demore mais de 20 segundos do que o limite de tempo, eu arranco seu cerebro")
        print("L UCHIHA: caso voce acerte menos que",numero_ganhar,"questoes, ou demore mais que o limite de tempo, eu levo", personagem, "e voce segue seu caminho")
        print("L UCHIHA: Você tem no maximo 3 tentativas para acertar cada questao!")
        input("(aperte enter para continuar)")
        print(nome+": Beleza! bora pro quiz!")
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("VALENDO!")
        usuario = "nada"
        contador_de_acertos = 0
        tempo1 = time.time()
        for i in questoes_fase_final:
            tentativas = 0
            while usuario != i[1] and tentativas<3:
                print(i[0])
                usuario = str(input("Resposta:"))
                tentativas+=1
            if tentativas <3:
                contador_de_acertos+=1
        tempo_demorado = time.time() - tempo1
        tempo_possivel = tempo_final+forca*10
        if contador_de_acertos >= numero_ganhar and tempo_demorado<tempo_possivel:
            print("L UCHIHA: Nao é possível...")
            time.sleep(1)
            print("L UCHIHA: Voce está em outro patamar...")
            time.sleep(1)
            print("L UCHIHA: pode levar", personagem, "e ir embora")
            time.sleep(1)
            return 2
        elif contador_de_acertos <numero_passar or tempo_demorado>(tempo_possivel+20) :
            print("L UCHIHA:PATETICO!")
            time.sleep(1)
            print("L UCHIHA: VOU TE ELIMINAR!")
            time.sleep(1)
            return -1
        else:
            perdidos.append(personagem)
            print("L UCHIHA: Bom, como voce nao passou por pouco")
            time.sleep(1)
            print("L UCHIHA:",personagem,"vai ficar cmg, mas voce pode ir pra sua jornada!")
            time.sleep(1)
            return 1
#morre pro vilao
def final(perdidos,nome):
    #morre pra propria tribo
    if len(perdidos) == 3:
        print("Ao chegar na vila sozinho, todo o seu povo percebe que está faltando algumas pessoas.")
        input("aperte enter pra continuar")
        print("Assim descobrem que todos morreram por causa de"+nome+".")
        input("aperte enter pra continuar")
        print("Povo: Todos morreram por sua causa! Voce nao sera perdoado! Está condenado a morte!")
        time.sleep(1)
        print("SUA TRIBO TE MATOU")
        print("GAME OVER (nota de desempenho: F)")
        input("aperte enter para continuar")
    elif len(perdidos) == 2:
        print("Ao chegar na vila sem",perdidos[0],"e",perdidos[1],"sua tribo de frustra um pouco.")
        input("aperte enter pra continuar")
        print("No entanto alguns entendem que voce se esforcou e outros nao, oque gera uma crise do seu relacionamento com o povo")
        input("aperte enter pra continuar")
        print("depois de dias de discussao, resolveram nao te matar, mas o clima continuou tenso pelo resto da vida.")
        time.sleep(1)
        print("FIM (nota de desempenho: B)")
        input("aperte enter para continuar")
    elif len(perdidos) == 1:
        if perdidos[0] != "seus pais":
            print("Ao chegar na vila, sua tribo se alegra em rever todos, menos os parentes de",perdidos[0])
            input("aperte enter pra continuar")
            print("parentes de "+perdidos[0]+": era pra voce ter o protegido... Mas sabemos que voce deu o seu melhor.")
            time.sleep(1)
            print("FIM QUASE PERFEITO (nota de desempenho: A)")
            input("aperte enter para continuar")
        else:
            print("Todos se alegram da chegada de voces na vila!")
            input("aperte enter pra continuar")
            print("Voce fica triste por um bom tempo por nao ter salvado seus pais, mas passa a lembrar de memorias boas com eles.")
            time.sleep(1)
            print("FIM QUASE PERFEITO (nota de desempenho: A)")
            input("aperte enter para continuar")
    else:
        print("Todos chegaram bem na tribo!")
        input("aperte enter pra continuar")
        print("foi realizada uma gigantesca festa e todos viveram felizes para sempre")
        time.sleep(1)
        print("PARABENS!!")
        print("FIM PERFEITO (nota de desempenho: S)")
        input("aperte enter para continuar")
def rodar():
    while True:
        game_over = 0
        print("BEM VINDO A AVENTURA PECULIARMENTE EDUCATIVA!")
        input("aperte enter pra continuar")
        print("Insira uma dificuldade, F, M ou I (fácil, medio ou impossivel respectivamente)")
        # variaveis
        dificuldade = str(input())
        if dificuldade == "M":
            dificuldade = 1
        elif dificuldade == "F":
            dificuldade = 0
        elif dificuldade == "I":
            dificuldade = 2
        # index 0 eh pergunta e index 1 eh resposta
        '''
        para nao gastar variaveis diferentes em cada dificuldade, vamos trabalhar com listas 
        na qual index 0 1 e 2 sao para facil medio e impossivel respectivamente
        '''
        medias_fase2 = [0.6, 0.8, 1]
        media_fase2 = medias_fase2[dificuldade]
        tempos_fase1 = [80, 40, 20]
        tempo_fase1 = tempos_fase1[dificuldade]
        tempos_final = [200,100,50]
        tempo_final = tempos_final[dificuldade]
        personagens = ["seus pais", "seu melhor amigo", "sua esposa"]
        perdidos = []
        print("Após anos de escravidao na tribo inimiga, você, alguns amigo e sua família")
        print("conseguem escapar, mas há muitos obstaculos que aguardam vocês no caminho de volta a tribo.")
        nome = str(input("Desculpa, esqueci seu nome! Insira ele porfavor: "))
        idade = int(input("Insira sua idade tambem(apenas o numero de anos): "))
        classe = int(input("escolha uma classe para essa aventura!(0 para Dev,1 para crossfiteiro,2 para genio prodigio,3 para nerd trincado)"))
        # inteligencia, forca
        classes = [["Dev", 2, 1], ["crossfiteiro", 0, 3], ["genio prodigio", 3, 0], ["nerd trincado", 1, 2]]
        nome_classe, inteligencia, forca = classes[classe]
        print()
        print("Legal! Estes são seus atributos!")
        print()
        mostra_atributos(nome, idade, nome_classe, inteligencia, forca,game_over)
        input("aperte enter pra continuar")
        pontos_evol = fase_xandao(tempo_fase1, personagens, perdidos, nome, forca)
        game_over = pontos_evol
        while pontos_evol > 0 and game_over != -1:
            print("como voce passou pelo vilão")
            print("voce tem direito de evoluir seus atributos")
            mostra_atributos(nome, idade, classe, inteligencia, forca,game_over)
            print("você tem", pontos_evol, "pontos para evoluir")
            atrib = int(input("digite 0 pra aprimorar inteligencia e 1 pra aprimorar a forca"))
            if 0 == atrib:
                inteligencia += 1
            if 1 == atrib:
                forca += 1
            pontos_evol -= 1
        mostra_atributos(nome, idade, classe, inteligencia, forca,game_over)
        pontos_evol = fase_newton(personagens,perdidos,nome,inteligencia,media_fase2,game_over)
        game_over = pontos_evol
        while pontos_evol > 0 and game_over != -1:
            print("como voce passou pelo vilão")
            print("voce tem direito de evoluir seus atributos")
            mostra_atributos(nome, idade, classe, inteligencia, forca,game_over)
            print("você tem", pontos_evol, "pontos para evoluir")
            atrib = int(input("digite 0 pra aprimorar inteligencia e 1 pra aprimorar a forca"))
            if 0 == atrib:
                inteligencia += 1
            if 1 == atrib:
                forca += 1
            pontos_evol -= 1
        pontos_evol = fase_final(personagens,perdidos,nome,inteligencia,forca,media_fase2,game_over,tempo_final)
        game_over = pontos_evol
        if game_over != -1:
            final(perdidos,nome)
        if game_over == -1:
            print("VOCE MORREU")
            print("GAME OVER (nota de desempenho: F)")
            input("aperte enter para continuar")
        print()
        print("Voce quer jogar denovo?(S/N)")
        jogar_denovo = str(input())
        if jogar_denovo == "N":
            print("JOGO DESLIGANDO")
            return
rodar()