import pygame
import time
import sys
import random
import os
pygame.init()

# NOTE: There are commented code related to snake tail which I was not able to satisfactorily implement
# Please ignore them or If you can make it work PLEASE DO

# Colors
white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,155,0)
blue  = (0,0,255)

# Display Size
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Title
pygame.display.set_caption('SnakeGame')

# Images
snakeHeadImg = pygame.image.load(os.path.join('images','snakeHead.png')).convert()
appleImg = pygame.image.load(os.path.join('images','apple.png')).convert()

pygame.display.set_icon(appleImg)

appleThickness = 30
block_size = 20
FPS = 10
clock = pygame.time.Clock()


def text_object(text,color,size):
    if size=='large':
        textSurface = largeFont.render(text,True,color)
    if size=='medium':
        textSurface = mediumFont.render(text,True,color)
    if size=='small':
        textSurface = smallFont.render(text,True,color)
    return textSurface, textSurface.get_rect()

smallFont = pygame.font.SysFont('comicsansms',25)
mediumFont = pygame.font.SysFont('comicsansms',50)
largeFont = pygame.font.SysFont('comicsansms',80)


def message_to_screen(msg, color, y_displ = 0,size = smallFont):
    '''MESSAGE TO SCREEN'''
    textSurface, textRect = text_object(msg, color,size)
    textRect.center = (display_width/2),(display_height/2 + y_displ)
    gameDisplay.blit(textSurface, textRect)
    







############################################################# make_snake ########################################################################

def make_snake(block_size, snakeList, direction):
    ''' Makes the snake object'''
    if direction == 'right':
        head = pygame.transform.rotate(snakeHeadImg, 270)
    elif direction == 'left':
        head = pygame.transform.rotate(snakeHeadImg, 90)
    elif direction == 'up':
        head = snakeHeadImg
    elif direction == 'down':
        head = pygame.transform.rotate(snakeHeadImg, 180)
    gameDisplay.blit(head, ((snakeList[-1][0],snakeList[-1][1])))


    ## for snake tail

    # tail = snakeTailImg
    # newDirection = directionList[-1]
    # if len(snakeList) == 3:
    #     olddir = directionList[0]
    #     directionList = [olddir,direction]
    # if len(snakeList) >= 3:
    #     newDirection = directionList[0]
    #     if snakeList[0][0] != snakeList[2][0] and snakeList[0][1] != snakeList[2][1]:
    #         newDirection = directionList[1]
    #         print(directionList)
    #         del directionList[0]
    # if newDirection == 'right':
    #     tail =  pygame.transform.rotate(snakeTailImg, 270)
    # elif newDirection == 'left':
    #     tail =  pygame.transform.rotate(snakeTailImg, 90)
    # elif newDirection == 'up':
    #     tail = snakeTailImg
    # elif newDirection == 'down':
    #     tail =  pygame.transform.rotate(snakeTailImg, 180)
        
    # gameDisplay.blit(tail, ((snakeList[0][0],snakeList[0][1])))     


    for XnY in snakeList[0:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])
##############################################################  END OF make_snake  #############################################################










def gameIntro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    intro = False

        gameDisplay.fill(white)
        message_to_screen("Snake Game", red,y_displ= -110, size = 'large')
        message_to_screen("Eat apples, don't crash, YOU KNOW THE DRILL!!", black,y_displ= 0, size = 'small')
        message_to_screen("Press C to play, Esc to pause and Q to quit", black,y_displ= 30, size = 'small')
        pygame.display.update()
        clock.tick(5)

def score(score):
    text = smallFont.render('Score: ' + str(score), True, black)
    gameDisplay.blit(text,[0,0])

def randAppleGen():
    randAppleX = random.randrange(0,display_width-appleThickness)
    # randAppleX = round(randAppleX/10.0)*10.0        #so that it comes in multiples of 10
    randAppleY = random.randrange(0,display_height-appleThickness)
    # randAppleY = round(randAppleY/10.0)*10.0
    return randAppleX,randAppleY




def pause():
    paused = True
    message_to_screen("Paused", red, y_displ=-50, size='large')
    message_to_screen("Press Q to quit", black, y_displ=0, size='small')
    message_to_screen("Press C to continue", black, y_displ=30, size='small')
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    quit()
        clock.tick(5)


#############################################################   GAMELOOP   ########################################################################
def gameLoop():
    # global directionList
    # directionList = ['right']
    gameExit = False
    gameOver = False
    #snake blocks
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = block_size
    lead_y_change = 0
    direction = 'right'
    snakeList = []
    snakeLength = 1

    #apple location
    randAppleX, randAppleY = randAppleGen()
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,y_displ=-30,size='large')
            message_to_screen(f'Score: {snakeLength-1}', black, y_displ=20, size='small')
            message_to_screen("Press C to play again. Press Q to quit", black, y_displ=50,size='small')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                if event.key == pygame.K_ESCAPE:
                    pause()
                if event.key == pygame.K_LEFT:
                    if direction != 'right':
                        direction = 'left'
                    # if direction != directionList[-1]:
                    #     directionList.append(direction)
                        lead_x_change = -block_size
                        lead_y_change = 0   
                elif event.key == pygame.K_RIGHT:
                    if direction != 'left':
                        direction = 'right'
                        # if direction != directionList[-1]:
                        #     directionList.append(direction)
                        lead_x_change = block_size
                        lead_y_change = 0
                elif event.key == pygame.K_UP:
                    if direction != 'down':
                        direction = 'up'
                        # if direction != directionList[-1]:
                        #     directionList.append(direction)
                        lead_y_change = -block_size
                        lead_x_change = 0

                elif event.key == pygame.K_DOWN:
                    if direction != 'up':
                        direction = 'down'
                        # if direction != directionList[-1]:
                        #     directionList.append(direction)
                        lead_y_change = block_size
                        lead_x_change = 0

        if lead_x >= display_width  or lead_x < 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        #it is often used to wipe the slate/surface clean
        gameDisplay.fill(white)

        #here we changes to the display
        gameDisplay.blit(appleImg, ((randAppleX),(randAppleY)))
        # pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,appleThickness,appleThickness])

        snakeHead = [lead_x,lead_y]
        snakeList.append(snakeHead)
        make_snake(block_size,snakeList,direction)
        if len(snakeList) > snakeLength:
            del(snakeList[0])

        #if snake "collides" with itself
        for segment in snakeList[:-1]:
            if segment == snakeHead:
                gameOver = True
    
        # NEW if snake "eats" the apple     
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX+appleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or  lead_y + block_size > randAppleY and lead_y + block_size < randAppleY+appleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        # the score function
        score(snakeLength-1)

        #frames per second(CHANGE IT AS LAST RESORT!!!! since it add burden to the processor)
        clock.tick(FPS)

        #once everything is done, AFTERWARDS update the display
        pygame.display.update()

    pygame.quit()
    sys.exit(0)
#----------------------------------------------------   END OF GAME LOOP   ------------------------------------------------------





gameIntro()
gameLoop()