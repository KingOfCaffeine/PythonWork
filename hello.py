import tkinter as tk
import math

class FractalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fractal Splitting in Half")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()
        self.draw_fractal(400, 500, -90, 100, 10)

    def draw_fractal(self, x, y, angle, length, depth):
        if depth == 0:
            return

        # Calculate the end point of the line segment
        x2 = x + int(math.cos(math.radians(angle)) * length)
        y2 = y + int(math.sin(math.radians(angle)) * length)

        # Draw the line segment
        self.canvas.create_line(x, y, x2, y2, fill="black")

        # Draw the next level of the fractal
        self.draw_fractal(x2, y2, angle - 30, length * 0.7, depth - 1)
        self.draw_fractal(x2, y2, angle + 30, length * 0.7, depth - 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = FractalApp(root)
    root.mainloop()
#work