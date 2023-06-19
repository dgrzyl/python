import pygame
import os
import math

WIDTH, HEIGHT = 1000, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pyracing')

BACKGROUND_COLOR = (3, 252, 132)

FPS = 60
VEL = 4
ROTATION_ANGLE = 2.2  # The angle by which the car rotates

TRACK = pygame.image.load(os.path.join('Assets', 'track.png'))
TRACK = pygame.transform.scale(TRACK, (768, 576))

CAR1 = pygame.image.load(os.path.join('Assets', 'car1.png'))
CAR1 = pygame.transform.scale(CAR1, (58, 32))

def draw_window(car, angle):
    WIN.fill(BACKGROUND_COLOR)
    rotated_car = pygame.transform.rotate(CAR1, angle)
    car_center = car.center
    rotated_rect = rotated_car.get_rect(center=car_center)
    WIN.blit(TRACK, (100, 10))
    WIN.blit(rotated_car, rotated_rect.topleft)
    pygame.display.update()

def main():
    car = pygame.Rect(500, 300, 58, 32)
    angle = 0  # Initial rotation angle
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            angle -= ROTATION_ANGLE
        if key_pressed[pygame.K_a]:
            angle += ROTATION_ANGLE

        # Convert the rotation angle to radians
        rad_angle = math.radians(angle)

        # Calculate the velocity components based on the rotation angle
        dx = VEL * math.cos(rad_angle)
        dy = VEL * math.sin(rad_angle)

        if key_pressed[pygame.K_s]:
            car.x += dx
            car.y -= dy
        if key_pressed[pygame.K_w]:
            car.x -= dx
            car.y += dy

        draw_window(car, angle)

    pygame.quit()

if __name__ == "__main__":
    main()
