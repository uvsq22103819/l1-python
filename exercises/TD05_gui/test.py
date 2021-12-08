from tkinter import * 

cycle_de_couleur = ['navy','crimson','ghostwhite','turquoise','midnightblue','darkcyan']


CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
root = Tk()
root.title('cercle')
canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg='white')
canvas.grid()

N = int(input("entrer un nombre"))
M=(CANVAS_HEIGHT/2, CANVAS_WIDTH/2)

for i in range(N):
    canvas.create_oval((CANVAS_WIDTH*i/N/2), (CANVAS_HEIGHT*i/N/2), (CANVAS_WIDTH-CANVAS_WIDTH*i/N/2), (CANVAS_HEIGHT-CANVAS_HEIGHT*i/N/2), fill = cycle_de_couleur[i%len(cycle_de_couleur)])

root.mainloop()