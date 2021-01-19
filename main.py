import pgzrun
import time
import random
speed = 3
WIDTH = 800
HEIGHT = 500

player = Actor('player')
alien = Actor('alien1', (100, 100))
laser_fire = Actor('laser1', (250, 200))
player.pos = (250, 200)

def draw():
  screen.blit('background', (0, 0))
  player.draw()
  alien.draw()
  laser_fire.draw()
  

def move_alien(alien):
  alien.right += 1
  if alien.left > WIDTH:
    alien.right = 0

  collide = laser_fire.colliderect(alien)
  print(collide)

  if collide == 0:
    print("missed me!")
  elif collide == 1:
    alien.image = "explosion4.png"

def move_player(player):
  if keyboard.left:
    player.x -= 1
    laser_fire.x -=1
  elif keyboard.right:
    player.x += 1
    laser_fire.x +=1
  elif keyboard.space:
    animate(laser_fire, pos =(alien.x, alien.y))
    screen.clear

def update():
  move_alien(alien)
  move_player(player)
  draw() 


pgzrun.go()