import pygame
import random

from pygame.constants import K_ESCAPE

#start screen
screen = pygame.display.set_mode((1000,800))

#start clock
clock = pygame.time.Clock()

#render text variables
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 32)
bigfont = pygame.font.SysFont('Comic Sans MS', 45)
giantfont = pygame.font.SysFont('Comic Sans MS', 80)

#initialize sprite class
class sprite(pygame.sprite.Sprite):
    def __init__(self, image, x:int, y:int):
        self.image = image
        self.x = x
        self.y = y
    def move(self, x ,y):
        self.x += x
        self.y += y

#initialize music
pygame.mixer.init()
pygame.mixer.music.load('24. Infernal Catharsis (Rebirth).mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
laser_sound = pygame.mixer.Sound('Final_laser_sfx_Michael_H.wav')
gunfire = pygame.mixer.Sound('Gunblasts.mp3')

enter = False
crashed = False
#start game
while True:

    #initialize varialbes
    time = 0
    score = 0
    gorrilla_num = []
    frequency = 0
    reload = False
    shot = True

    monkey = sprite(pygame.image.load('Monkey.gif'), 20, 300)
    jungle = sprite(pygame.image.load('Forest Fire.jpeg'), 0, 0)
    laser = sprite(pygame.image.load('Laserbeam.png'), 20, monkey.y)
    choose_background = random.randint(1,10)
    if choose_background == 1:
        jungle = sprite(pygame.image.load('Burning Forest.jpeg'), 0 , 0)

    
    while not crashed:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True 


        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load('Forest Fire.jpeg'), (0, 0))
        screen.blit(giantfont.render("Press Enter To Start", False, (255, 255, 255)), (230, 400))
        if time%24 in range(1,4):
            screen.blit(monkey.image, (monkey.x, monkey.y))
        elif time%24 in range(4,8):
            screen.blit(pygame.image.load('Monkey-2 (dragged).tiff'), (monkey.x, monkey.y))
        elif time%24 in range(8,12):
            screen.blit(pygame.image.load('Monkey-3 (dragged).tiff'), (monkey.x, monkey.y))
        elif time%24 in range(12,16):
            screen.blit(pygame.image.load('Monkey-4 (dragged).tiff'), (monkey.x, monkey.y))
        elif time%24 in range(16,20):
            screen.blit(pygame.image.load('Monkey-5 (dragged).tiff'), (monkey.x, monkey.y))
        elif time%24 in range(20, 24) or time%24 == 0:
            screen.blit(pygame.image.load('Monkey-6 (dragged).tiff'), (monkey.x, monkey.y))
        if time%36 in range(0,3):
            screen.blit(pygame.image.load("Gorrila-1 (dragged).tiff"), (700, 300))
        elif time%36 in range(3,6):
            screen.blit(pygame.image.load("Gorrila-2 (dragged).tiff"), (700, 300))
        elif time%36 in range(6,9):
            screen.blit(pygame.image.load("Gorrila-3 (dragged).tiff"), (700, 300))
        elif time%36 in range(9,12):
            screen.blit(pygame.image.load("Gorrila-4 (dragged).tiff"), (700, 300))
        elif time%36 in range(12,15):
            screen.blit(pygame.image.load("Gorrila-5 (dragged).tiff"), (700, 300))
        if time%36 in range(15,18):
            screen.blit(pygame.image.load("Gorrila-6 (dragged).tiff"), (700, 300))
        elif time%36 in range(18,21):
            screen.blit(pygame.image.load("Gorrila-7 (dragged).tiff"), (700, 300))
        elif time%36 in range(21,24):
            screen.blit(pygame.image.load("Gorrila-8 (dragged).tiff"), (700, 300))
        elif time%36 in range(24,27):
            screen.blit(pygame.image.load("Gorrila-9 (dragged).tiff"), (700, 300))
        elif time%36 in range(27,30):
            screen.blit(pygame.image.load("Gorrila-10 (dragged).tiff"), (700, 300))
        elif time%36 in range(30,33):
            screen.blit(pygame.image.load("Gorrila-11 (dragged).tiff"), (700, 300))
        elif time%36 in range(33,36):
            screen.blit(pygame.image.load("Gorrila-12 (dragged).tiff"), (700, 300))
        pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_RETURN] and enter == False:
            print("break")
            break
        if not pygame.key.get_pressed()[pygame.K_RETURN] and enter == True:
            enter = False
        breakout = False
        if pygame.key.get_pressed()[K_ESCAPE]:
            breakout = True
            break
        time += 1

    if breakout == True:
        break
    
    time = 0
    set_time = 0
    gun_time = 0
    while not crashed:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True 

        clock.tick(200)
        fps = clock.get_fps()

        screen.fill((255,255,255))
        screen.blit(jungle.image, (0, 0))
        screen.blit(bigfont.render("Score: " + str(score), False, (255, 255, 255)),(860, 50))
        screen.blit(bigfont.render("FPS" + str(int(clock.get_fps())), False, (255, 255, 255)), (860, 110))
       
        if set_time == 300:
            reload = False

        if time%24 in range(1,4):
            screen.blit(monkey.image, (monkey.x, monkey.y))
        elif time%24 in range(4,8):
            screen.blit(pygame.image.load('Monkey-2 (dragged).tiff'), (monkey.x, monkey.y))
        elif time%24 in range(8,12):
            screen.blit(pygame.image.load('Monkey-3 (dragged).tiff'), (monkey.x, monkey.y))
        elif time%24 in range(12,16):
            screen.blit(pygame.image.load('Monkey-4 (dragged).tiff'), (monkey.x, monkey.y))
        elif time%24 in range(16,20):
            screen.blit(pygame.image.load('Monkey-5 (dragged).tiff'), (monkey.x, monkey.y))
        elif time%24 in range(20, 24) or time%24 == 0:
            screen.blit(pygame.image.load('Monkey-6 (dragged).tiff'), (monkey.x, monkey.y))
        
        if pygame.key.get_pressed()[K_ESCAPE]:
            esc = True
            break
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP] and fps != 0:
            monkey.move(0, -3  * 110/clock.get_fps())
        if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN] and fps != 0:
            monkey.move(0, 3 * 110/clock.get_fps())
        if pygame.key.get_pressed()[pygame.K_q] and fps != 0 and shot==True:
            screen.blit(laser.image, (120, monkey.y-200+random.randint(-10, 10)))
            pygame.mixer.Sound.play(laser_sound)
            laser_sound.set_volume(0.25)
            if not len(gorrilla_num) == 0:
                for i in gorrilla_num:
                    if i[1] < monkey.y+150 and i[1] > monkey.y-250:
                        i[2] -= 15 * 100/clock.get_fps()       
        else:
            pygame.mixer.Sound.stop(laser_sound)
        if (random.randint(1,400-frequency) == 1 and len(gorrilla_num) < 3):
            gorrilla_num.append([1000, random.randint(-100, 600), random.randint(200+int(time/10),1000+int(time/10)), False])
        if random.randint(1, 2000) == 1 and len(gorrilla_num) < 3:
            gorrilla_num.append([1000, random.randint(-100, 600), 2000+3*int(time/10), True])
        if not frequency > 350:
            frequency = int(time/25)

        if not len(gorrilla_num) == 0:
            for i in gorrilla_num:
                if time%36 in range(0,3):
                    screen.blit(pygame.image.load("Gorrila-1 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(3,6):
                    screen.blit(pygame.image.load("Gorrila-2 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(6,9):
                    screen.blit(pygame.image.load("Gorrila-3 (dragged).tiff"), (i[0], i[1]))

                elif time%36 in range(9,12):
                    screen.blit(pygame.image.load("Gorrila-4 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(12,15):
                    screen.blit(pygame.image.load("Gorrila-5 (dragged).tiff"), (i[0], i[1]))
                if time%36 in range(15,18):
                    screen.blit(pygame.image.load("Gorrila-6 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(18,21):
                    screen.blit(pygame.image.load("Gorrila-7 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(21,24):
                    screen.blit(pygame.image.load("Gorrila-8 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(24,27):
                    screen.blit(pygame.image.load("Gorrila-9 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(27,30):
                    screen.blit(pygame.image.load("Gorrila-10 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(30,33):
                    screen.blit(pygame.image.load("Gorrila-11 (dragged).tiff"), (i[0], i[1]))
                elif time%36 in range(33,36):
                    screen.blit(pygame.image.load("Gorrila-12 (dragged).tiff"), (i[0], i[1]))
                if i[3] == False and fps != 0:
                    i[0] -= 4 * 100/clock.get_fps()
                elif fps != 0:
                    i[0] -= 2 * 100/clock.get_fps()

        if pygame.key.get_pressed()[pygame.K_e] and reload == False:
            gunfire.play()
            gunfire.set_volume(0.3)
            if shot == True:
                gun_time = 0
            if gun_time == 500:
                set_time = 0
                gunfire.stop()
                reload = True
            shot = False

            pygame.draw.line(screen, (255, 255, 0), (monkey.x+350, monkey.y+50), pygame.mouse.get_pos())
            pygame.draw.line(screen, (255, 255, 0), (monkey.x+360, monkey.y+60), pygame.mouse.get_pos())
            pygame.draw.line(screen, (255, 255, 0), (monkey.x+340, monkey.y+40), pygame.mouse.get_pos())

            if time%10 in range(0,2):
                screen.blit(pygame.transform.flip(pygame.image.load('gunfire-28 (dragged).tiff'), True, False), (monkey.x+100, monkey.y))
            if time%10 in range(2,4):
                screen.blit(pygame.transform.flip(pygame.image.load('gunfire-29 (dragged).tiff'), True, False), (monkey.x+100, monkey.y))
            if time%10 in range(4,6):
                screen.blit(pygame.transform.flip(pygame.image.load('gunfire-30 (dragged).tiff'), True, False), (monkey.x+100, monkey.y))
            if time%10 in range(6,8):
                screen.blit(pygame.transform.flip(pygame.image.load('gunfire-31 (dragged).tiff'), True, False), (monkey.x+100, monkey.y))
            if time%10 in range(8,10):
                screen.blit(pygame.transform.flip(pygame.image.load('gunfire-32 (dragged).tiff'), True, False), (monkey.x+100, monkey.y)) 

            if time % 2 == 0  and fps != 0:
                if not len(gorrilla_num) == 0:
                    for i in gorrilla_num:
                        pos = pygame.mouse.get_pos()
                        if (int(i[0]) in range(int(pos[0])-300, int(pos[0])-100) and (int(i[1]) in range(int(pos[1])-200, int(pos[1])))):
                            i[2] -= 70 * 100/clock.get_fps()
                            screen.blit(pygame.image.load('BOOM.png'), (pos[0]-30, pos[1]-40))
        elif not pygame.key.get_pressed()[pygame.K_e] and shot == False:
            gunfire.stop()
            set_time = 0
            reload = True
            shot = True

        if monkey.y < -160:
            monkey.y = 850
        if monkey.y > 850:
            monkey.y = -160

        getout = False
        for i in gorrilla_num:
            if i[2] <= 0:
                gorrilla_num.remove(i)
                score += 1
            if i[0] <= -200:
                getout = True
        if getout == True:
            break

        time += 1
        if reload == True:
            screen.blit(bigfont.render("Reloading:" + str(300-set_time), False, (255, 255, 255)), (750, 150))
            set_time += 1
        if shot == False:
            gun_time += 1

        pygame.display.flip()
    
    pygame.mixer.Sound.stop(laser_sound)
    pygame.mixer.Sound.stop(gunfire)
    goback = False
    breakout = False
    while not crashed:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        
        screen.blit(giantfont.render("Game Over", False, (255, 255, 255)),(350, 400))
        pygame.display.flip()
        goback = False
        breakout = False
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            enter = True
            goback = True
            break
        if pygame.key.get_pressed()[K_ESCAPE] and esc == False:
            breakout = True
            break
        if not pygame.key.get_pressed()[K_ESCAPE]:
            esc = False
    
    if goback == True:
        continue
    if breakout == True:
        break


pygame.quit()
quit()