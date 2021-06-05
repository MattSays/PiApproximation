import pygame
import random
import os

WINDOW_SIZE = 500

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

MAX_POINTS = 1000000
STEP = MAX_POINTS / 1000

circle_points = 0
points = 0

# Checking if point is in circle (inscribed in the window square)
def calculate_circle_condition(pos):
    return ((pos[0]-WINDOW_SIZE/2)**2 + (pos[1]-WINDOW_SIZE/2)**2) <= (WINDOW_SIZE/2)**2

# Calculates and draw black point at random x and y positions until the total number of points exceeds the limit
# Whetever a point is in the circle, it is drawn with green and the amount of circle points
# Every a specified amount of steps, drawn points are shown on screen 
def draw_random_point(canvas, window):
    global points
    global circle_points
    
    if points < MAX_POINTS: 
        pos = (random.random() * WINDOW_SIZE, random.random() * WINDOW_SIZE)
        
        color = BLACK
        
        points += 1
        
        if calculate_circle_condition(pos):
            circle_points += 1
            color = GREEN 

        if points % STEP == 0 : 
            os.system('clear') # Used to clear screen on unix systems
            print('Circle points amount: {}\t Points amount: {}'.format(circle_points, points))
            print(4 * (circle_points / points))
            window.blit( canvas, ( 0, 0 ) )
            pygame.display.flip()
            
        
        pygame.draw.circle(canvas, color, pos, 1)
        
    
def run_app():
    pygame.init()

    # Set up the drawing window
    pygame.display.set_caption('Pi approximation')
    window = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])

    canvas = pygame.Surface( ( WINDOW_SIZE, WINDOW_SIZE ) )
    canvas.fill( WHITE )

    # Run until the user asks to quit
    running = True

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 

        draw_random_point(canvas, window)



    # Done! Time to quit.
    pygame.quit()


run_app()