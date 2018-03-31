import pygame
import time

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class Game(object):
    def main(self, screen):
        
        image = pygame.image.load('arrow.png')
        image = pygame.transform.scale(image, (800,800))
        image_x = 550
        image_y = 100
        angle = 0
        keyPress = False        

        screen.fill((255, 255, 255))                       #set the background to white
        #arrow_image = rot_center(image, angle)            #only use if you want to show the arrow pointing up on the screen before any presses.
        #screen.blit(arrow_image, (image_x, image_y))
        pygame.display.flip()
        
        

        while keyPress == False:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        keyPress = True
                        while angle > -90:
                            angle = -90                                    #change the values to anywhere between 5-15 to show the arrow turning in that direction.
                            screen.fill((255, 255, 255))
                            arrow_image = rot_center(image, angle)            
                            screen.blit(arrow_image, (image_x, image_y))
                            pygame.display.flip()
                    if event.key == pygame.K_a:
                        keyPress = True
                        while angle < 90:
                            angle = 90                                     #change the values to anywhere between 5-15 to show the arrow turning in that direction.
                            screen.fill((255, 255, 255))
                            arrow_image = rot_center(image, angle)            
                            screen.blit(arrow_image, (image_x, image_y))
                            pygame.display.flip()
                if event.type == pygame.QUIT:
                    return 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
     
            #screen.fill((255, 255, 255))                                      ##################
            #arrow_image = rot_center(image, angle)                            KEEP THESE COMMENTED OUT UNLESS YOU WANT THE ARROW POINTING UP AT THE START
            #screen.blit(arrow_image, (image_x, image_y))                      otherwise, the default is set to display a white screen only. 
            #pygame.display.flip()                                             ##################

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    Game().main(screen)
                    return
                    
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((1280, 720)) for windowed mode
    Game().main(screen)