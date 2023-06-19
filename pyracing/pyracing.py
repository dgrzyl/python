import pygame
import os
import math

WIDTH, HEIGHT = 1000, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pyracing')

BACKGROUND_COLOR = (3, 252, 132)

FPS = 60
VEL = 3.6
ROTATION_ANGLE = 2.2  # The angle by which the car rotates

TRACK = pygame.image.load(os.path.join('Assets', 'track.png'))
TRACK = pygame.transform.scale(TRACK, (768, 576))

CAR1 = pygame.image.load(os.path.join('Assets', 'car1.png'))
CAR1 = pygame.transform.scale(CAR1, (58, 32))

#CAR1_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'engine-6000.mp3'))

CAR2 = pygame.image.load(os.path.join('Assets', 'car2.png'))
CAR2 = pygame.transform.scale(CAR2, (58, 32))

def draw_window(car1, angle1):
    WIN.fill(BACKGROUND_COLOR)
    rotated_car1 = pygame.transform.rotate(CAR1, angle1)
    car1_center = car1.center
    rotated_rect = rotated_car1.get_rect(center=car1_center)
    WIN.blit(TRACK, (100, 10))
    WIN.blit(rotated_car1, rotated_rect.topleft)
    pygame.display.update()

def main():
    car1 = pygame.Rect(500, 300, 58, 32)
    angle1 = 0  # Initial rotation angle
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            angle1 -= ROTATION_ANGLE
        if key_pressed[pygame.K_a]:
            angle1 += ROTATION_ANGLE

        # Convert the rotation angle to radians
        rad_angle = math.radians(angle1)

        # Calculate the velocity components based on the rotation angle
        dx = VEL * math.cos(rad_angle)
        dy = VEL * math.sin(rad_angle)

        if key_pressed[pygame.K_s]:
            car1.x += dx
            car1.y -= dy
        if key_pressed[pygame.K_w]:
            car1.x -= dx
            car1.y += dy
            #CAR1_SOUND.play()

        draw_window(car1, angle1)

    pygame.quit()

if __name__ == "__main__":
    main()
