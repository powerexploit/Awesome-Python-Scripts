#Imports and dependencies
import pygame
import random
import numpy as np
import time

#Constants
BLACK = (0, 0, 0)
DEAD = 0
ALIVE = 1
CAN_REPRODUCE = 3
CAN_SURVIVE = 2
N = 15
DEAD_COLOR = (76, 0, 153) #violet
LIVE_COLOR = (255 , 255 , 102) #yellow
WAIT_TIME = 4
EDGE = 38
BOARD_SIZE = 600
clock = pygame.time.Clock()

#This function returns the nearest neighbours of a particular cell, whether it lives or not is determined by the rules
def nearest_neighbours(universe , i , j ,N):
        
    def above(universe , i , j , N):
        return(universe[(i - 1)% N][(j - 1)% N] + universe[(i - 1)% N][j] + universe[(i - 1)% N][(j + 1)% N])
    
    def below(universe ,i ,j ,N):
        return(universe[(i + 1)% N][(j - 1)% N] + universe[(i + 1)% N][j] + universe[(i + 1)% N][(j + 1)% N])

    def right_and_left(universe ,i , j , N):
        return(universe[i][(j + 1)% N] + universe[i][(j - 1)% N])
    
    return(above(universe ,i ,j ,N) + below(universe ,i ,j ,N) + right_and_left(universe ,i ,j ,N))

#This function implements whether the cell will be alive or dead in a particular iteration
def game_of_life(universe):
  current_gen = universe.copy()
  for i in range(N):
    for j in range(N):
      state_of_cell = universe[i][j]
      number_alive = nearest_neighbours(universe , i , j ,N)
      if state_of_cell == DEAD:
        if number_alive == CAN_REPRODUCE:
         current_gen[i][j] = ALIVE
      else:
        if number_alive > CAN_REPRODUCE or number_alive < CAN_SURVIVE:
         current_gen[i][j] = DEAD
  
  universe[:] = current_gen[:]
  return(universe)

def display_board(iterations):
    #The PyGame module is loaded the simulation begins
    pygame.init()
    size = (BOARD_SIZE, BOARD_SIZE)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("CONWAYS'S Game of Life")
    universe = np.random.randint(2 , size = N*N).reshape((N,N))
    for iteration in range(iterations):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        screen.fill(BLACK)
        universe = game_of_life(universe)
        for i in range(N):
            for j in range(N):
                if universe[i][j] == 0:
                    pygame.draw.rect(screen, DEAD_COLOR , [i*40, j*40, EDGE, EDGE], 0)
                else:
                   pygame.draw.rect(screen, LIVE_COLOR , [i*40, j*40, EDGE, EDGE], 0)
        pygame.display.update()
        time.sleep(WAIT_TIME)
    pygame.quit()

if __name__ == "__main__":
    #The user is prompted to enter the number of iterations the simulation should run
    iterations = int(input("Enter number of iterations : "))
    display_board(iterations)
