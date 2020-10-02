'''resolvi comentar o codigo em ingles para treinar
'''
import pygame
pygame.init()
window = pygame.display.set_mode((500,480))
pygame.display.set_caption("First game project")

clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 7.5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y+11,29,52) #one hit box for each class (top left x, top left y,width,height)
        self.visible = True
        self.health = 10
        self.able_to_shot =True
    def draw(self,window):
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))  # image three coordinates for one image and his coordinate
                self.walkCount += 1

            elif self.right:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:  # if the character stops we shoot the bullet in the last direction
                if self.right:
                    window.blit(walkRight[0],(self.x,self.y))
                else:
                    window.blit(walkLeft[0],(self.x,self.y))
            pygame.draw.rect(window, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)),10))  # drawing two rectangles (red and green) to represent the health
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            #pygame.draw.rect(window,(255,0,0),self.hitbox,2) #to draw the hitbox around the character
    def hit(self):
        if self.health > 0:
            self.health -=1
        else:
            self.able_to_shot = False
            self.visible = False
            self.hitbox = (0,0, 31, 57)
            #self.win()
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 18*facing

    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)
class enemy:
    walkRight = [pygame.image.load('images/R1E.png'), pygame.image.load('images/R2E.png'), pygame.image.load('images/R3E.png'), pygame.image.load('images/R4E.png'), pygame.image.load('images/R5E.png'), pygame.image.load('images/R6E.png'), pygame.image.load('images/R7E.png'), pygame.image.load('images/R8E.png'), pygame.image.load('images/R9E.png'),pygame.image.load('images/R10E.png'),pygame.image.load('images/R11E.png')]
    walkLeft = [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'),
                pygame.image.load('images/L3E.png'), pygame.image.load('images/L4E.png'),
                pygame.image.load('images/L5E.png'), pygame.image.load('images/L6E.png'),
                pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'),
                pygame.image.load('images/L9E.png'),pygame.image.load('images/L10E.png'),pygame.image.load('images/L11E.png')]
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x,end]
        self.end = end
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x+17,self.y+2,31,57)
        self.health = 10
        self.visible = True
    def draw(self,window):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33: #because we have 11 images
                self.walkCount = 0
            if self.vel > 0: #walking to the right
                window.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            else:
                window.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            pygame.draw.rect(window, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (255,0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) #drawing two rectangles (red and green) to represent the health
            self.hitbox = (self.x+16,self.y+2,31,57)
            #pygame.draw.rect(window,(255,0,0),self.hitbox,2) #to draw the hitbox around the characte

    def move(self):
        if self.vel>0: #moving to the right
            if self.x < self.path[1]+self.vel:
                self.x+=self.vel
            else:
                self.vel = self.vel*-1
                self.x+=self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel*-1
                self.x += self.vel
                self.walkCount = 0
    def hit(self):
        if self.health > 0:
            self.health -=1
        else:
            self.visible = False
            self.hitbox = (0,0, 31, 57)
            self.x ,self.y = 0,0

score = 0 #1 point for every bullet that hits the enemy,
font = pygame.font.SysFont("comicsans",30,True)
#font, size, bold?

pygame.mixer.music.load("balada.mp3")
pygame.mixer.music.play(-1, start = 280)
#pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.30)
#this determine which way the character will walk and then we output the correct image
bullet_sound = pygame.mixer.Sound("laser.wav")
#let  use lists to store the images
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
background = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')
x = 50
y = 400
width = 40
height = 60
bullets = []  #list for put and remove them if they have left the window
bullet_cdr = 0 #cooldown for bullets
#let's do a function for loop and draw the scene
def redrawGameWindow():
    window.blit(background,(0,0))
    main_character.draw(window)
    goblin.draw(window)
    if goblin.visible and main_character.visible:
        text = font.render("Score: "+str(score),1,(0,0,0))
        window.blit(text,(390,10))
    for bullet in bullets:
        bullet.draw(window)
    if not goblin.visible:
        text = font.render("YOU WON ", 1, (0, 0, 0))
        window.blit(text, (180, 180))
    if not main_character.visible:
        font2 = pygame.font.SysFont("comicsans",60,True)
        text = font2.render("SEU BOT, PERDEU! ", 1, (0, 0, 0))
        window.blit(text, (30, 180))
    pygame.display.update()

goblin = enemy(100,410,64,64,300)
main_character = player(x,y,width,height)
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y - bullet.radius > goblin.hitbox[1]:
            if bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2] and bullet.x - bullet.radius > goblin.hitbox[0]:
                goblin.hit()
                score+=1
                bullets.pop(bullets.index(bullet))
        if bullet.x<500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet)) #remove from the list
    if main_character.x > goblin.x - 30 and main_character.x < goblin.x +30:
        if main_character.y > goblin.y - 30 and main_character.y <goblin.y +30:
            main_character.hit()
            print("ai")
    keys = pygame.key.get_pressed() #this will give us a dictionary where each key has a value of 0 or 1. Where 1 is pressed and 0 is not
    if keys[pygame.K_q]:
        int(input("entre"))
    if main_character.able_to_shot:
        if keys[pygame.K_SPACE]:
            if main_character.left:
                facing = -1
            else:
                facing = 1
            if bullet_cdr <= 0: #limit of 5 bullets on the screen
                bullets.append(projectile(round(main_character.x+main_character.width//2), #the bullet starts from the middle of the character
                                          round(main_character.y + main_character.height//2),6,(0,0,0),facing))
                bullet_cdr = 15
                bullet_sound.play()
    if keys[pygame.K_LEFT] and main_character.x > main_character.vel: #We can check if a key is pressed like this and making sure that the object will never get out of the screen
        main_character.x-= main_character.vel
        main_character.left = True
        main_character.right = False
        main_character.standing = False
    elif keys[pygame.K_RIGHT] and main_character.x < 500 - main_character.width - main_character.vel:
        main_character.x+=main_character.vel
        main_character.left = False
        main_character.right = True
        main_character.standing = False
    else: #reset the walkcounter if the character is not moving
        main_character.standing = True
        main_character.walkCount = 0
    if not main_character.isJump:
        if  keys[pygame.K_UP]:
            main_character.isJump = True
            main_character.right = False
            main_character.left = False
            main_character.walkCount = 0
    else:
        if main_character.jumpCount >= -7.5: #jumping and falling
            main_character.y -=  (main_character.jumpCount * abs(main_character.jumpCount)) * 0.5
            main_character.jumpCount -=1
        else: #ending and reset  values of the jump
            main_character.jumpCount = 7.5
            main_character.isJump = False
    bullet_cdr -=1
    redrawGameWindow()
pygame.quit()