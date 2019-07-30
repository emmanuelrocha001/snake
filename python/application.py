import pygame
import sys
import math
from random import randint
from copy import deepcopy
from PIL import Image
from os import path

COLOR_WHITE = [ 255, 255, 255]

def windowSetup( window_size ):
  icon = pygame.image.load(path.join ( 'images', 'icon.png'))
  pygame.display.set_icon( icon )
  pygame.display.set_caption( 'snake' )
  screen = pygame.display.set_mode ( window_size )
  screen.fill ( COLOR_WHITE )

  return screen

def loadAssets():
  pass




  
def main():


  # pause mode
  #--------------------------------------------------------------
  clock = pygame.time.Clock()
  pause_game = False
  #--------------------------------------------------------------

  # game init
  #--------------------------------------------------------------
  pygame.init()
  screen_size = [ int( sys.argv[1] ) , int( sys.argv[2] ) ] 
  print(screen_size)
  screen = windowSetup( screen_size )
  

  # game loop
  while 1:

    clock.tick( 30 )

    pygame.display.flip()



    for event in pygame.event.get():
      # watch for exit button press
      if event.type == pygame.QUIT: sys.exit()

      # Watch for esc key press
      if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_ESCAPE :
          sys.exit()



if ( __name__ == '__main__'):
  main()