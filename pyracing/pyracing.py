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

#CAR1_SOUND = pygame.mixer.Sound('Assets/engine-6000.wav')

CAR2 = pygame.image.load(os.path.join('Assets', 'car2.png'))
CAR2 = pygame.transform.scale(CAR2, (58, 32))

def draw_window(car1, angle1, car2, angle2):
    WIN.fill(BACKGROUND_COLOR)
    rotated_car1 = pygame.transform.rotate(CAR1, angle1)
    rotated_car2 = pygame.transform.rotate(CAR2, angle2)
    car1_center = car1.center
    car2_center = car2.center
    rotated_rect = rotated_car1.get_rect(center=car1_center)
    rotated_rect2 = rotated_car2.get_rect(center=car2_center)
    WIN.blit(TRACK, (100, 10))
    WIN.blit(rotated_car1, rotated_rect.topleft)
    WIN.blit(rotated_car2, rotated_rect2.topleft)
    pygame.display.update()


def main():
    #pygame.mixer.init()  # Initialize the audio mixer
    car1 = pygame.Rect(370, 280, 58, 32)
    car2 = pygame.Rect(400, 240, 72, 33.51)
    angle1 = -35  # Initial rotation angle
    angle2 = 145
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

        if key_pressed[pygame.K_RIGHT]:
            angle2 -= ROTATION_ANGLE
        if key_pressed[pygame.K_LEFT]:
            angle2 += ROTATION_ANGLE

        # Convert the rotation angle to radians
        rad_angle = math.radians(angle1)
        rad_angle2 = math.radians(angle2)

        # Calculate the velocity components based on the rotation angle
        dx = VEL * math.cos(rad_angle)
        dy = VEL * math.sin(rad_angle)

        fx = VEL * math.cos(rad_angle2)
        fy = VEL * math.sin(rad_angle2)

        if key_pressed[pygame.K_s]:
            car1.x += dx
            car1.y -= dy
        if key_pressed[pygame.K_w]:
            car1.x -= dx
            car1.y += dy
            #CAR1_SOUND.play()

        if key_pressed[pygame.K_UP]:
            car2.x += fx
            car2.y -= fy
        if key_pressed[pygame.K_DOWN]:
            car2.x -= fx
            car2.y += fy
            #CAR1_SOUND.play()

        draw_window(car1, angle1, car2, angle2)

    pygame.quit()

if __name__ == "__main__":
    main()
