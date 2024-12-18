import pygame
from src.elements.ui import bezier
import numpy as np

class LovePointer():
    def __init__(self, game, angle):
        self.game = game
        self.sprite = pygame.Surface((300, 10), pygame.SRCALPHA)
        pygame.draw.rect(self.sprite, (255, 0, 0), self.sprite.get_rect())
        self.rect = self.sprite.get_rect(midbottom=(game.game_width/2-self.sprite.get_width()/2, game.game_height/2 + 35 ))
        self.angle = 0
        self.finalAngle = angle
        self.elapsedTime = 0
        self.duration = 10  # Duration of the movement in seconds
        self.control_points = np.array([
            [0, 0],
            [0.3, 0],
            [0, 1],
            [1, 1]
        ])
        self.bezierPoints = bezier.generate_bezier_curve(self.control_points)

    def update(self, dt, actions):
        self.elapsedTime += dt
        t = min(self.elapsedTime / self.duration, 1)  # Normalize time to range [0, 1]
        eased_t = bezier.get_y_for_x(t, self.bezierPoints)

        if (self.angle < self.finalAngle):
            self.angle = eased_t * self.finalAngle


    def render(self, surface):
        # Define the pivot point (e.g., the bottom center of the sprite)
        pivot = (self.rect.right, self.rect.centery)

        # Calculate the offset from the pivot to the center of the sprite
        offset_center_to_pivot = pygame.math.Vector2(self.rect.center) - pivot

        # Rotate the offset vector
        rotated_offset = offset_center_to_pivot.rotate(self.angle)

        # Calculate the new center position
        rotated_center = (pivot[0] + rotated_offset.x, pivot[1] + rotated_offset.y)

        # Rotate the image
        rotated_image = pygame.transform.rotate(self.sprite, -self.angle)
        new_rect = rotated_image.get_rect(center=rotated_center)

        # Draw the rotated image
        surface.blit(rotated_image, new_rect.topleft)