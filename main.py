import sys
import os
import subprocess
import pygame
from src import game

def restart_game():
    # Ensure Pygame is properly quit before restarting
    pygame.quit()
    subprocess.Popen([sys.executable] + sys.argv)  # Start a new game process
    sys.exit()  # Exit the current process cleanly

if __name__ == "__main__":
    while True:  # This loop will keep restarting the game after it ends
        g = game.Game()
        g.game_loop()
        # After the game ends, decide whether to restart or exit
        print("Game Over. Restarting the game...")

        # Restart the game using a function call
        restart_game()  # Restart the game or exit cleanly
