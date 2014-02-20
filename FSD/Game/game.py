import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
running = True
x = pygame.image.load('X.png')
x = pygame.transform.smoothscale (x, (40, 40))
o = pygame.image.load('O.png')
o = pygame.transform.smoothscale(o, (40, 40))
o_posx = 280
o_posy = 280
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #if the close button on screen is clicked
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #if Escape key is pressed down
            running = False

        screen.fill((200, 200, 200))
        screen.blit(o, (o_posx, o_posy))
        pygame.display.flip()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if o_posx < 500:
                o_posx += 40
                screen.blit(o, (o_posx, o_posy))
                pygame.display.flip()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    if o_posx > 100:
                        o_posx -= 40
                        screen.blit(o, (o_posx, o_posy))
                        pygame.display.flip()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if o_posy > 100:
                        o_posy -= 40
                        screen.blit(o, (o_posx, o_posy))
                        pygame.display.flip()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    if o_posy < 500:
                        o_posy += 40
                        screen.blit(o, (o_posx, o_posy))
                        pygame.display.flip()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            o2 = pygame.image.load('O.png')
            screen.blit(o2, (o_posx, o_posy))
            pygame.display.flip()
            print("test")
            #not working. Why?

#the following is just a test
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        if o_posy < 500:
            o_posy += 40
            screen.blit(o, (o_posx, o_posy))
            pygame.display.flip()

    if key[pygame.K_RIGHT]:
        if o_posx < 500:
                o_posx += 40
                screen.blit(o, (o_posx, o_posy))
                pygame.display.flip()

    if key[pygame.K_LEFT]:
        if o_posx > 100:
            o_posx -= 40
            screen.blit(o, (o_posx, o_posy))
            pygame.display.flip()

    if key[pygame.K_UP]:
        if o_posy > 100:
            o_posy -= 40
            screen.blit(o, (o_posx, o_posy))
            pygame.display.flip()

