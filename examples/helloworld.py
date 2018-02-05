import pygame # Adds Pygame to the code
import view # Adds View to the code
pygame.init() # Initalizes Pygame
app = view.ViewPort(0, 0) # Creates View object registry
screen = pygame.display.set_mode([600, 600]) # Creates Pygame window
viewSquare = app.addObj(300, 300, None) # Adds square to View object registry
squareID = viewSquare[0] # Saves the square's ID to squareID
squareInfo = pygame.Rect(app.getX(squareID), app.getY(squareID), 50, 50)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60) # Sets FPS to 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Listens for when use hits space
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                app.setDirection("left") # Sets View camera direction to left
    screen.fill([255, 255, 255]) # Clears screen
    app.updateStats(4) # Tells View to update the registry
    squareInfo = pygame.Rect(app.getX(squareID), app.getY(squareID), 50, 50)
    pygame.draw.rect(screen, [0, 0, 0], squareInfo, 0) # Draws square
    pygame.display.flip() # Draws everything to screen
pygame.quit()
