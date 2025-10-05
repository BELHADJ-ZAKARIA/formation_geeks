import tkinter as tk
import random

class GameOfLife:
    def __init__(self, master, rows=25, cols=40, cell_size=20):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        # Canvas with white background
        self.canvas = tk.Canvas(master, width=cols*cell_size, height=rows*cell_size, bg="white")
        self.canvas.pack()

        # Random grid 0/1
        self.grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        self.rects = [[None for _ in range(cols)] for _ in range(rows)]

        # Draw initial cells
        self.draw_cells()

        # Start animation loop
        self.update()

    def count_neighbors(self, x, y):
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),          (0,1),
                      (1,-1), (1,0), (1,1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                count += self.grid[nx][ny]
        return count

    def step(self):
        new_grid = [[0]*self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                n = self.count_neighbors(i, j)
                if self.grid[i][j] == 1 and n in (2, 3):
                    new_grid[i][j] = 1
                elif self.grid[i][j] == 0 and n == 3:
                    new_grid[i][j] = 1
        self.grid = new_grid

    def draw_cells(self):
        """Draw black grid lines and fill cells."""
        self.canvas.delete("all") 
        for i in range(self.rows):
            for j in range(self.cols):
                x1, y1 = j*self.cell_size, i*self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                color = "black" if self.grid[i][j] else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="grey")

    def update(self):
        """Refresh display each 150ms."""
        self.step()
        self.draw_cells()
        self.master.after(150, self.update)


# --- Run the game ---
root = tk.Tk()
root.title("Game of Life")
game = GameOfLife(root, rows=25, cols=40, cell_size=20)
root.mainloop()