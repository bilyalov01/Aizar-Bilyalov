import pygame
import random

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')

icon = pygame.image.load("tank1.png")
pygame.display.set_icon(icon)

background_img = pygame.image.load("background.png").convert()
tank1_img = pygame.image.load("tank1.png").convert()
tank2_img = pygame.image.load("tank2.png").convert()
bullet_img = pygame.image.load("bullet.png").convert()
explosion_img = pygame.image.load("explosion.png").convert()

tank1_img.set_colorkey((0,0,0))
tank2_img.set_colorkey((0,0,0))
bullet_img.set_colorkey((0,0,0))
explosion_img.set_colorkey((255,255,255))

clock = pygame.time.Clock()

direction1 = 1
direction2 = 1

tank_height = 30
tank_width = 30
class Tank():

    global tank_height, tank_width, display_height, display_width

    def __init__(self, x, y, color, image):
        self.tank_x = x
        self.tank_y = y
        self.tank_color = color
        self.dx = 100
        self.dy = 100
        self.bullets = []
        self.bullets_num = 0

        self.make_shoot = False
        self.shooting = False

        self.bullet_x = -500
        self.bullet_x = -500
        self.cooldown = 0
        self.lifes = 3
        self.image = image
        
    def moving(self, direction, seconds):
        
        if direction == 1:
            #меняет положение наверх
            self.dy = -100
            self.dx = 0
            self.tank_y += self.dy * seconds
            if (self.tank_y < -tank_height):
                self.tank_y = display_height + tank_height
            #pygame.draw.rect(display, self.tank_color , (self.tank_x, self.tank_y, tank_width, tank_height))
            turn = pygame.transform.rotate(self.image, 90)
            display.blit(turn,(self.tank_x, self.tank_y, tank_width, tank_height))

        if direction == 2:
            #вниз
            self.dy = 100
            self.dx = 0
            self.tank_y += self.dy * seconds
            if (self.tank_y - display_height) > tank_height:
                self.tank_y = -tank_height
            #pygame.draw.rect(display, self.tank_color, (self.tank_x, self.tank_y, tank_width, tank_height))
            turn = pygame.transform.rotate(self.image, 270)
            display.blit(turn,(self.tank_x, self.tank_y, tank_width, tank_height))
            

        if direction == 3:
            #направо
            self.dy = 0
            self.dx = 100
            self.tank_x += self.dx * seconds
            if (self.tank_x - display_width ) > tank_width:
                self.tank_x = -tank_width
            #pygame.draw.rect(display, self.tank_color, (self.tank_x, self.tank_y, tank_width, tank_height))
            display.blit(self.image,(self.tank_x, self.tank_y, tank_width, tank_height))

        if direction == 4:
            #налево
            self.dy = 0
            self.dx = -100
            self.tank_x += self.dx * seconds
            if (self.tank_x < -tank_width):
                self.tank_x = display_width+tank_width
            #pygame.draw.rect(display, self.tank_color, (self.tank_x, self.tank_y, tank_width, tank_height))
            flip = pygame.transform.flip(self.image, 1, 0)
            display.blit(flip,(self.tank_x, self.tank_y, tank_width, tank_height))

    def make_bullets(self):
        
        self.bullets_number = 0
        self.bullets.clear()

        self.bullet_x = self.tank_x + 20
        self.bullet_y = self.tank_y + 20
        
        for i in range (50):
            self.bullet_x += (self.dx)//5
            self.bullet_y += (self.dy)//5
            self.bullets.append(self.bullet_x)
            self.bullets.append(self.bullet_y)


        pygame.mixer.music.load('shoot.mp3')
        pygame.mixer.music.play(0)
        
        self.make_shoot = False
        self.shooting = True

    def show_bullets(self):

        if self.bullets_number < 100:
            self.bullet_x = self.bullets[self.bullets_number]
            self.bullet_y = self.bullets[self.bullets_number+1]
            #pygame.draw.rect(display, (0, 0, 255), (self.bullet_x,self.bullet_y, 10, 10))
            display.blit(bullet_img,(self.bullet_x,self.bullet_y))
            self.bullets_number +=2
        else:
            self.bullet_x = -500
            self.bullet_y = -500
            self.bullets_number = 0
            self.bullets.clear()
            self.shooting = False

class Button():
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.inactive_colour = (99, 115, 128)
        self.active_colour = (64, 81, 97)
    
    def draw(self, x, y, message, action = None, font_size = 30):
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed()
        
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display,self.active_colour ,(x, y, self.width, self.height))
                
                
            if click[0] == 1:
                pygame.mixer.music.load('button.mp3')
                pygame.mixer.music.play(0)
                pygame.time.delay(300)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()

        
        else:
            pygame.draw.rect(display,self.inactive_colour ,(x, y, self.width, self.height))

        print_text(message = message,x = x + 10, y = y + 10, font_color=(0,0,0),font_size = font_size)

def show_menu():
    menu_bckgr = pygame.image.load('menu.png')
    
    start_bt = Button(288, 70)
    exit_bt = Button(120, 70)
    
    pygame.mixer.music.load('main_theme.mp3')
    pygame.mixer.music.play(0)
    show = True
  
    while show:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0, 0))
        start_bt.draw(270, 200, 'Start Game', start_game_button, 50)
        exit_bt.draw(358, 300, 'Exit', quit, 50)
        pygame.display.update()
        clock.tick(45)

def start_game_button():
    while run_game():
        pass

milliseconds = clock.tick(60)
seconds = milliseconds / 1000.0

def run_game():

    global direction1, direction2
    
    game = True

    tank1 = Tank(100,100,(255,0,0), tank1_img)
    tank2 = Tank(700, 500, (0,255,0), tank2_img)

    win_first = False
    win_second = False
       
    #button = Button(100, 50)
    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False
                elif event.key == pygame.K_UP:
                    direction1 = 1
                elif event.key == pygame.K_DOWN:
                    direction1 = 2
                elif event.key == pygame.K_RIGHT:
                    direction1 = 3
                elif event.key == pygame.K_LEFT:
                    direction1 = 4
                elif event.key == pygame.K_w:
                    direction2 = 1
                elif event.key == pygame.K_s:
                    direction2 = 2
                elif event.key == pygame.K_d:
                    direction2 = 3
                elif event.key == pygame.K_a:
                    direction2 = 4
                elif event.key == pygame.K_RETURN:
                    tank1.make_shoot = True
                elif event.key == pygame.K_SPACE:
                    tank2.make_shoot = True

        #display.fill((255,255,255))
        display.blit(background_img, (0,0))
      
        #движeниe
        tank1.moving(direction1, seconds)
        tank2.moving(direction2, seconds)
        # Выстрел
        if tank1.make_shoot:
            if (tank1.cooldown == 0):
                tank1.make_bullets()
                tank1.cooldown = 100
        if tank2.make_shoot:
            if (tank2.cooldown == 0):
                tank2.make_bullets()
                tank2.cooldown = 100
        # Кулдаун
        if tank1.cooldown > 0:
            tank1.cooldown -= 1
        if tank2.cooldown > 0:
            tank2.cooldown -= 1
        
        # Полет пули
        if tank1.shooting:
            tank1.show_bullets()
            win_first = collision(tank1, tank2)
        if tank2.shooting:
            tank2.show_bullets()
            win_second = collision(tank1, tank2)

        # Попадание и количество жизней
        if win_first:
            if tank2.lifes != 0:
                tank2.lifes -= 1
                tank1.bullets_number = 100
                if tank2.lifes == 0:
                    print_text('Player 1 win. Press TAB to play again, ESC to exit', display_width//2-350, display_height//2, (255,255,255), 30)
                    game = False
        if win_second:
            if tank1.lifes != 0:
                tank1.lifes -= 1
                tank2.bullets_number = 100
                if tank1.lifes == 0:
                    print_text('Player 2 win. Press TAB to play again, ESC to exit', display_width//2-350, display_height//2, (255,255,255), 30)
                    game = False
            
        #строка кол-ва жизней и кулдаун
        print_text('Player 1. Lifes: {}'.format(tank1.lifes), 15, 15, (255, 0, 0), 22)
        print_text('Player 2. Lifes: {}'.format(tank2.lifes), display_width-200, 10,(0, 255, 0), 22)

        print_text('Cooldown: {}'.format(int(tank1.cooldown/10)), 10, 30, (255, 0, 0), 22)
        print_text('Cooldown: {}'.format(int(tank2.cooldown/10)), display_width-200, 30,(0, 255, 0), 22)

        pygame.display.update()
        clock.tick(60)

    return pause()

def collision(tank1, tank2):
    
    if ((tank1.bullet_x + 5 > tank2.tank_x) and (tank1.bullet_x + 5 < (tank2.tank_x + 30)) and
        (tank1.bullet_y + 5> tank2.tank_y) and (tank1.bullet_y + 5 < (tank2.tank_y + 30))):

        pygame.mixer.music.load('vzryv.mp3')
        pygame.mixer.music.play(0)

        #tank1.shooting = False
        display.blit(explosion_img, (tank2.tank_x-20,tank2.tank_y-20))
        
        return True
    
    elif ((tank2.bullet_x +5> tank1.tank_x) and (tank2.bullet_x + 5 < (tank1.tank_x + 30)) and
        (tank2.bullet_y + 5> tank1.tank_y) and (tank2.bullet_y + 5 < (tank1.tank_y + 30))):        

        pygame.mixer.music.load('vzryv.mp3')
        pygame.mixer.music.play(0)

        for i in range (100):
            display.blit(explosion_img, (tank1.tank_x-20,tank1.tank_y-20))
        
        return True
    
    else:
        return False

def pause():
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            return True
        if keys[pygame.K_ESCAPE]:
            return False
        
        pygame.display.update()
        clock.tick(15)

def print_text(message,x, y, font_color, font_size):
    font_type = 'PingPong.ttf'
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x,y))
show_menu()
while run_game():
    pass

pygame.quit()