import pygame
from random import randint
from os.path import join

#general setup
pygame.init ()

#Creating Display Surface
Window_Width, Window_Height = 1280, 720
display_Surface = pygame.display.set_mode ( ( Window_Width, Window_Height ) )
display_Title = pygame.display.set_caption ( 'Space Shooter' )

#Creating Clock for Fixed Frame Rate
clock = pygame.time.Clock()

#Generating Plane Surface
surf = pygame.Surface ( ( 60, 30 ) )

#Importing Image as Surface For Player
Player_Surf = pygame.image.load ( join ( 'Games', 'Assets', '5games-main', 'space shooter', 'images', 'player.png' ) ) .convert_alpha ()
Player_Rect = Player_Surf.get_frect ( center = ( Window_Width / 2, Window_Height * 3/4 ) )
Player_Direction = pygame.math.Vector2 ( 2, -1 )
Player_Speed = 10

#Importing Image as Surface for stars
Star_Surf = pygame.image.load(join('Games', 'Assets', '5games-main', 'space shooter', 'images', 'star.png')).convert_alpha()
Star_Position = [(randint(0, Window_Width), randint(0, Window_Height)) for i in range(20)]

#importing Image as Surface for Meteor
Meteor_Surf = pygame.image.load ( join ( 'Games', 'Assets', '5games-main', 'space shooter', 'images', 'meteor.png' ) )
Meteor_Rect = Meteor_Surf.get_frect ( center = ( Window_Width / 2, Window_Height * 1/4 ) )

#importing Image as Surface for Laser Beam
Laser_Beam_Surf = pygame.image.load ( join ( 'Games', 'Assets', '5games-main', 'space shooter', 'images', 'laser.png' ) )
Laser_Beam_Rect = Laser_Beam_Surf.get_frect ( bottomright = ( Window_Width - 20, Window_Height - 20 ) )

#Bool for Game Status Indication
running = True

while running:
    
    #Clock for Frame Rate
    clock.tick(30)

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Draw The Game
    #Changing the Background Colour
    display_Surface.fill('black')
    
    #Printing The Stars
    for pos in Star_Position:
        display_Surface.blit(Star_Surf, pos)
        
    #Printing the Laser Beam
    display_Surface.blit ( Laser_Beam_Surf, Laser_Beam_Rect )
    
    #Player Movement and Animation
    Player_Rect.center += (Player_Direction * Player_Speed)

    #Player Surface over Display Surface
    display_Surface.blit ( Player_Surf, Player_Rect )
    
    #Object Surface over Display Surface
    display_Surface.blit ( Meteor_Surf, Meteor_Rect )
    
    #Update The Entire Display Surface
    pygame.display.update()
            
pygame.quit()