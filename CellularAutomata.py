import pygame
import random
import time

# Simulation And Application Settings
height = 400
width = 600
cellSize = 2
generationTimestep = 10 # In ms!
rulesetcode = 193 # This will be used initially

# Initialize the game engine
pygame.init()

# Set the height and width and title of the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cellular Automata Test")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Initial conditions for the cells. All 0 with center cell as 1
cells = [0 for e in range(width/cellSize)]
cells[len(cells)/2] = 1

# This returns the new generation cell given a cell (middle) and it's neighbours
def rules(left, middle, right):
    neighbourhood = [left, middle, right]
    # RuleIndex is the decimal form of the (binary) neighbourhood. Used to acces a new cell from the ruleset array.
    ruleIndex = int(''.join(str(e) for e in neighbourhood), 2)
    # This converts the rulesetcode (decimal) into an 8 bit number represented as a list
    ruleset = list('{0:08b}'.format(rulesetcode))
    ruleset.reverse()
    # Access the state of the new cell from the ruleset using our index
    return int(ruleset[ruleIndex])

generation = 0
print("Current Rule: {0:d} ({0:08b})".format(rulesetcode))
# Initially set the screen to all white
screen.fill((255, 255, 255))

# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    
    # Loop through the cells in the current generation drawing each
    for i, cell in enumerate(cells):
        if cell == 1:
            # If the cell size is a single pixel we can't use rect to draw it
            if cellSize > 1:
                pygame.draw.rect(screen, (0, 0, 0), [i*cellSize, cellSize*generation, cellSize, cellSize])
            else:
                screen.set_at((i*cellSize, cellSize*generation), (0, 0, 0))

    # Loop through the cells, grabbing it's neighbours and calculate the subsequent generation
    newcells = []
    for i, cell in enumerate(cells):
        # This modular maths wraps the index if were at the edge of the screen
        left = cells[(i-1) % len(cells)]
        middle = cell
        right = cells[(i+1) % len(cells)]
        newstate = rules(left, middle, right)
        # We use newcells so we don't overwrite cells while we're still using it
        newcells.append(newstate)
    cells = newcells

    # If we've filled the screen then pick a new rule and reset everything
    if (cellSize*generation) >= height:
        rulesetcode = random.randint(0, 255)
        generation = 0
        time.sleep(2)
        pygame.display.flip()
        screen.fill((255, 255, 255))
        cells = [0 for e in range(width/cellSize)]
        cells[len(cells)/2] = 1
        print("Current Rule: {0:d} ({0:08b})".format(rulesetcode))
    else:            
        # Update only part of the screen so previous generations are left untouched
        pygame.display.update([0, cellSize*generation, width, height])
        generation += 1

    # Wait until the next generation
    clock.tick(1000/generationTimestep)
    
# Be IDLE friendly
pygame.quit()