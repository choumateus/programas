import turtle
import winsound
#tela
tela = turtle.Screen()
tela.title("Pong")
tela.bgcolor("black")
tela.setup(width= 800, height=600)
tela.tracer(0)

#******     jogador 1   *****
barra1 = turtle.Turtle() #objeto
barra1.speed(0)
barra1.shape("square" )
barra1.color("white")
barra1.shapesize(5,1)
barra1.penup()
barra1.goto(-350,0) #coordenadas

# **********    jogador 2   ***********
barra2 = turtle.Turtle() #objeto
barra2.speed(0)
barra2.shape("square" )
barra2.color("white")
barra2.shapesize(5,1)
barra2.penup()
barra2.goto(350,0) #coordenadas

# ********** bola **************
bola = turtle.Turtle() #objeto
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0,0) #coordenadas
bola.dx = 0.2 #direcoes e velocidade
bola.dy = 0.2

#*********  funcoes *****************

def barra1_pra_cima():
    y = barra1.ycor()
    y += 20 #coordenadas de y mais 20
    barra1.sety(y) #jogando a barra para cima

def barra1_pra_baixo():
    y = barra1.ycor()
    y -= 20 #coordenadas de y mais 20
    barra1.sety(y) #jogando a barra para cima

def barra2_pra_cima():
    y = barra2.ycor()
    y += 20 #coordenadas de y mais 20
    barra2.sety(y) #jogando a barra para cima

def barra2_pra_baixo():
    y = barra2.ycor()
    y -= 20 #coordenadas de y mais 20
    barra2.sety(y) #jogando a barra para cima



#criando o placar
caneta = turtle.Turtle()
caneta.speed(0)
caneta.color("white")
caneta.penup()
caneta.hideturtle()
caneta.goto(0,260)
caneta.write("Jogador1: 0  Jogador2: 0", align = "center", font=("Courier", 24, "normal"))
pontos_jogador1= 0
pontos_jogador2=0


#*********  conexao com o teclado   ***********
tela.listen()
tela.onkeypress(barra1_pra_cima, "w")
tela.onkeypress(barra1_pra_baixo, "s")
tela.onkeypress(barra2_pra_cima, "Up")
tela.onkeypress(barra2_pra_baixo, "Down")

#loop do jogo
while True:
    tela.update()

    #bola se mexe

    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #quando a bola atinge os topos
    if bola.ycor() > 290:
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
        bola.sety(290)
        bola.dy *= -1
    if bola.ycor() < -290:
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
        bola.sety(-290)
        bola.dy *= -1
    if bola.xcor() > 390:
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
        bola.goto(0,0)
        bola.dx *= -1
        pontos_jogador1+=1
        caneta.clear()
        caneta.write("Jogador1: "+ str(pontos_jogador1)+"  Jogador2: "+ str(pontos_jogador2), align="center", font=("Courier", 24, "normal"))
    if bola.xcor() < -390:
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
        bola.goto(0,0)
        bola.dx *= -1
        pontos_jogador2+=1
        caneta.clear()
        caneta.write("Jogador1: " + str(pontos_jogador1) + "  Jogador2: " + str(pontos_jogador2), align="center",
                     font=("Courier", 24, "normal"))

    #quando a bola atinge a barra
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < barra2.ycor() + 50 and bola.ycor() > barra2.ycor() - 50 ):
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
        bola.setx(340)
        bola.dx *= -1
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barra1.ycor() + 50 and bola.ycor() > barra1.ycor() - 50):
        winsound.PlaySound("test.wav", winsound.SND_ASYNC)
        bola.setx(-340)
        bola.dx *= -1

