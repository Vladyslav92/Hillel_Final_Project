import pygame
import Buttons
from pygame.locals import *
import process
from os import path

pygame.init()
pygame.mixer.init()

img_dir = path.join(path.dirname(__file__), 'images')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 480
HEIGHT = 600

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


class MainWindow:
    def __init__(self):
        self.main()

    def display(self):
        self.background = pygame.image.load("images/starfield.png")
        self.background_rect = self.background.get_rect()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption("Space Time")

    def update_display(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background_rect)
        process.draw_text(self.screen, "Space Time", 64, WIDTH / 2, HEIGHT / 4)
        # Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, BLUE, 190, 250, 100, 50, 0, "PLAY", BLACK)
        self.Button2.create_button(self.screen, BLUE, 190, 350, 100, 50, 0, "QUIT", BLACK)
        pygame.display.flip()

    def main(self):
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        process.SpaceTime()
                if event.type == MOUSEBUTTONDOWN:
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        exit(process.SpaceTime)
                        pygame.quit()


class ShowGoScreen:
    def __init__(self, scores):
        self.scores = scores
        self.show()

    def display(self):
        self.background = pygame.image.load("images/starfield.png")
        self.background_rect = self.background.get_rect()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption("Space Time")

    def updated_display(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background_rect)
        process.draw_text(self.screen, "Game Over!", 64, WIDTH / 2, HEIGHT / 4)
        process.draw_text(self.screen, "Your Score - {}".format(self.scores), 34, WIDTH / 2, HEIGHT / 6)
        process.draw_text(self.screen, "Arrow keys move, Space to fire", 22, WIDTH / 2, HEIGHT / 2)
        pygame.display.flip()

    def show(self):
        self.display()
        while True:
            self.updated_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


class VictoryScreen:
    def __init__(self, scores):
        self.scores = scores
        self.show()

    def display(self):
        self.background = pygame.image.load("images/starfield.png")
        self.background_rect = self.background.get_rect()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption("Space Time")

    def updated_display(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background_rect)
        process.draw_text(self.screen, "Victory!", 64, WIDTH / 2, HEIGHT / 4)
        process.draw_text(self.screen, "Your Score - {}".format(self.scores), 34, WIDTH / 2, HEIGHT / 6)
        process.draw_text(self.screen, "Congratulations!", 22, WIDTH / 2, HEIGHT / 2)
        self.Button1.create_button(self.screen, BLUE, 190, 350, 100, 50, 0, "PLAY", BLACK)
        self.Button2.create_button(self.screen, BLUE, 190, 450, 100, 50, 0, "QUIT", BLACK)
        pygame.display.flip()

    def show(self):
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
        self.display()
        while True:
            self.updated_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        process.SpaceTime()
                if event.type == MOUSEBUTTONDOWN:
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        exit(process.SpaceTime)
                        pygame.quit()


if __name__ == '__main__':
    obj = MainWindow()
