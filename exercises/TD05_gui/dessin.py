import tkinter as tk
import random
from tkinter.constants import N

root = tk.Tk()
root.title('dessin')
CANVAS_WIDTH, CANVAS_HEIGHT =600,600


couleur = ['red','pink','yellow','orange','brown','blue','black','cyan','white','green','grey','purple','magenta','violet','chocolate','tomato','mediumslateblue','navy','crimson','ghostwhite','turquoise','midnightblue','darkcyan','indigo','firebrick','lightcoral','saddlebrown','deepskyblue','mediumspringgreen','mediumturquoise','gold','cornflowerblue','lime','olive','salmon','orangered','darkorange','lightsalmon','slateblue','hotpink','plum','lavenderblush','palevioletred','olivedrab','seagreen','lemonchiffon','maroon','mistyrose','mintcream','wheat','navajowhite','bisque','darkslategray','blueviolet','fuchsia','darkolivegreen','paleturquoise','aliceblue','lightgoldenrodyellow']
color=random.choice(couleur)

# Bouton quitter
btn = tk.Button(root, text='Quitter', command=root.quit, bg="pink")




#bouton cercle

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg='black')
canvas.grid(row=2, column=2, rowspan=4 ,columnspan=3)


def cercle():
    x=random.randint(0,500)
    y=random.randint(0,500)
    canvas.create_oval(x, y, x+100, y+100,fill=color)



tp = tk.Button(root,text='rond', command=cercle)

#bouton carré

def carre():
    x=random.randint(-100,600)
    y=random.randint(-100,600)
    canvas.create_rectangle(x+50,y+150,x+150,y+50, fill=color)

pt = tk.Button(root,text='carré',command=carre)


#bouton croix
def croix():
    x=random.randint(0,500)
    y=random.randint(0,500)
    canvas.create_rectangle(x+60,y,x+90,y+150, fill=color)
    canvas.create_rectangle(x,y+60,x+150,y+90, fill=color)


ftg= tk.Button(root,text='croix',command=croix)



#bouton couleur

def change_color():
    global color
    color=random.choice(couleur)
       
    
    

qb = tk.Button(root,text='choisir une couleur',command=change_color)






# Placement du bouton dans «root»
pt.grid(row=3,column=0)
tp.grid(row=2, column=0)
btn.grid(row=0,column=0)
qb.grid(row=0, column=2)
ftg.grid(row=4, column=0)




# Lancement de la «boucle principale»
root.mainloop()

