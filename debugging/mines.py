#!/usr/bin/python3
"""
mines.py - Minesweeper game with win detection
Fixed version: Adds win condition detection
"""

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.won = False

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        
        self.revealed[y][x] = True
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        
        # Check for win after each reveal
        self.check_win()
        return True

    def check_win(self):
        """Check if all non-mine cells have been revealed"""
        total_cells = self.width * self.height
        mine_count = len(self.mines)
        revealed_count = sum(sum(row) for row in self.revealed)  # Count True values
        
        # Win condition: all non-mine cells are revealed
        if revealed_count == total_cells - mine_count:
            self.won = True
            self.game_over = True

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Coordinates must be between 0 and {self.width-1}")
                    continue
                
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    self.game_over = True
                    break
                
                if self.won:
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
                    
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
