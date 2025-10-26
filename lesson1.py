import pygame
import random

#ekranga yozuv chiqarish uchun yozish shart
pygame.font.init()

#ekran o'lchami
WIDTH,HEIGHT = 900,600
PLAYER_WIDTH,PLAYER_HEIGHT = 60,60
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 5
font = pygame.font.SysFont('normal', 30)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Dodge')
bg = pygame.transform.scale(pygame.image.load('./image/l1_background.png', 'background'), (WIDTH, HEIGHT))
def draw(player, stars):
    #blit rasm chizish uchun
    window.blit(bg, (0, 0))
    #bu yerda rang berildi
    pygame.draw.rect(window, 'red', player)
    for star in stars:
        pygame.draw.rect(window, 'yellow', star)
    pygame.display.update()

def main():
    run = True
    hit = False
    #player nomli shakl yaratildi
    player = pygame.Rect(WIDTH//2, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    #bu tezligi sekin,tez komputerlarda ham 1xil ishlashi uchun
    clock = pygame.time.Clock()
    #yulduz chiqish tezligi
    star_add_increment = 200
    star_count = 0
    starts=[]
    while run:
        #tick sanaydigan metod/60=60 sekund
        star_count+= clock.tick(60)
        #yulduzlar chiqish tezligi
        if star_count>star_add_increment:
            #har kelganda chiqish soni
            for _ in range(3):
                #random joylashuvda chiqishi
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                starts.append(star)
            star_add_increment = max(200, star_add_increment-50)
            star_count=0
        for event in pygame.event.get():
            #exit bosilsa chiqib ketadigan qilish
            if event.type == pygame.QUIT:
                run=False
                break
        #bosilgan tugmalar
        keys = pygame.key.get_pressed()
        #bu yerda chap taraf devordan o'tib kelishini oldini oldim
        if keys[pygame.K_LEFT] and player.x-PLAYER_VEL>=0:
            player.x-=PLAYER_VEL
        #bu yerda esa shuni o'ng tarafi
        if keys[pygame.K_RIGHT] and player.x+PLAYER_VEL+player.width<=WIDTH:
            player.x+=PLAYER_VEL
        #           copied list
        for star in starts[:]:
            star.y+=STAR_VEL
            if star.y>HEIGHT:
                starts.remove(star)
            elif star.y + star.height >=player.y and star.colliderect(player):
                starts.remove(star)
                hit = True
                break
        if hit:
            lost_text = font.render('You lost !', 1, 'white')
            window.blit(lost_text, (WIDTH/2-lost_text.get_width()/2, HEIGHT/2-lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        #bu yerda esa u chizilyapti
        draw(player, starts)
    pygame.quit()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt as error:
        print(error)