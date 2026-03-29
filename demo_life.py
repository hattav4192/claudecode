import os
import time
import random

WIDTH, HEIGHT = 40, 20

def make_grid():
    return [[random.choice([0, 0, 0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def count_neighbors(grid, y, x):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            ny, nx = (y + dy) % HEIGHT, (x + dx) % WIDTH
            count += grid[ny][nx]
    return count

def next_gen(grid):
    new = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            n = count_neighbors(grid, y, x)
            alive = grid[y][x]
            if alive:
                row.append(1 if n in (2, 3) else 0)
            else:
                row.append(1 if n == 3 else 0)
        new.append(row)
    return new

def render(grid, gen):
    lines = [f"\033[1;36m Conway's Game of Life  Gen: {gen:04d} \033[0m"]
    lines.append("\033[90m+" + "-" * WIDTH + "+\033[0m")
    for row in grid:
        line = "\033[90m|\033[0m"
        for cell in row:
            line += "\033[1;33m#\033[0m" if cell else " "
        line += "\033[90m|\033[0m"
        lines.append(line)
    lines.append("\033[90m+" + "-" * WIDTH + "+\033[0m")
    lines.append("\033[90mCtrl+C で終了\033[0m")
    print("\033[H" + "\n".join(lines), end="", flush=True)

def main():
    grid = make_grid()
    gen = 0
    print("\033[2J\033[?25l", end="")  # clear + hide cursor
    try:
        while True:
            render(grid, gen)
            grid = next_gen(grid)
            gen += 1
            time.sleep(0.1)
            if gen % 200 == 0:
                grid = make_grid()  # refresh to avoid stagnation
    except KeyboardInterrupt:
        print("\033[?25h\033[0m\n終了しました。")

if __name__ == "__main__":
    main()
