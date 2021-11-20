import pygame,random,sys
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
wood = pygame.image.load("gallery/Wood_BG.png")
crosshair = pygame.image.load("gallery/Crosshair.png")
water = pygame.image.load("gallery/Water_BG.png")
duck = pygame.image.load("gallery/Duck.png")
font = pygame.font.Font(None,60)
text = font.render("You won",True,(0,0,0))
text_rect = text.get_rect(center = (640,360))
cloud1 = pygame.image.load("gallery/Cloud1.png")
cloud2 = pygame.image.load("gallery/Cloud2.png")
duck_list = []
for i in range(0,20):
    x = random.randrange(100,1200)
    y = random.randrange(300,600)
    duck_rect = duck.get_rect(center = (x,y))
    duck_list.append(duck_rect)
water_y = 600
speed = 2.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index,duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):
                    del duck_list[index]
    screen.blit(wood,(0,0))
    screen.blit(cloud1,(100,100))
    screen.blit(cloud1,(500,50))
    screen.blit(cloud1,(1100,150))
    screen.blit(cloud2,(700,100))
    screen.blit(cloud2,(900,250))
    water_y += speed
    if water_y >= 700 or water_y <= 500:
         speed *= -1
    screen.blit(water,(0,water_y))
    for duck_rect in duck_list:
        screen.blit(duck,duck_rect)
    screen.blit(crosshair,crosshair_rect)
    if duck_list == []:
        screen.blit(text,text_rect)
        
    pygame.display.update()
    clock.tick(120)

    
