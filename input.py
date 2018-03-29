import pygame

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
        clock = pygame.time.Clock()
        
        image = pygame.image.load('arrow.png')
        image_x = 160
        image_y = 120
        angle = 0
        
        
        while 1:
            clock.tick(60)

            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                
            
            key = pygame.key.get_pressed()
            if key[pygame.K_b]:
                angle = -90
            elif key[pygame.K_a]:
                angle = 90
            elif key[pygame.K_c]:
                angle = 0
            
            
            arrow_image = rot_center(image, angle)            
            screen.fill((255, 255, 255))
            screen.blit(arrow_image, (image_x, image_y))
            pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().main(screen)