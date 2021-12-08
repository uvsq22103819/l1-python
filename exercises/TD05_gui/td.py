import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH / 2
y = CANVAS_HEIGHT / 2
canvas.create_line(y, x1+100, y, x0-50)
canvas.create_oval(x0 +50, y -150, x0 + 150, y - 50)
canvas.create_oval(x1 - 150, y +150, x1 -50, y +50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    

root.mainloop()


