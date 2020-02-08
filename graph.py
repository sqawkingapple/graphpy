import pygame, gui, easygui, sys, random

def Graph(xmax, ymax, xinterval, function):

    stop = False
    x = -xmax
    testx = x - xinterval
    pygame.init()
    fps = 120
    clock = pygame.time.Clock()
    w, h = 500, 500
    display = pygame.display.set_mode((w,h))
    xaxis = pygame.Surface((w,1))
    yaxis = pygame.Surface((1,h))
    xaxis.fill((255,255,255))
    yaxis.fill((255,255,255))
    display.blit(xaxis, (0,h//2))
    display.blit(yaxis, (w//2,0))

    while True:

        tempfunction = list(function)

        if stop == False:
            for i in tempfunction:
                if i == "x":
                    tempfunction[tempfunction.index(i)] = ("("+str(x)+")")
            convfunction = str(''.join([str(j) for j in tempfunction]))

        if stop == False:
            y = eval(str(convfunction))
        if stop == False:
            pygame.draw.circle(display,(255,255,255),[int(x*(w//2/xmax)+w//2),int(y*-(h//2/ymax)+h//2)],1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if stop == False: x += xinterval
        testx = x - xinterval
        if x >= xmax:
            stop = True
        if stop == True:
            fps = 10
        print((int(x*(w//2/xmax)+w//2),int(y*-(h//2/ymax)+h//2)))
        pygame.display.flip()
        clock.tick(fps)
