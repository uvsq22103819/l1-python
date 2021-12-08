import tkinter as tk

couleur = ['red','pink','yellow','orange','brown','blue','black','cyan','white','green','grey','purple','magenta','violet','chocolate','tomato','mediumslateblue','navy','crimson','ghostwhite','turquoise','midnightblue','darkcyan','indigo','firebrick','lightcoral','saddlebrown','deepskyblue','mediumspringgreen','mediumturquoise','gold','cornflowerblue','lime','olive','salmon','orangered','darkorange','lightsalmon','slateblue','hotpink','plum','lavenderblush','palevioletred','olivedrab','seagreen','lemonchiffon','maroon','mistyrose','mintcream','wheat','navajowhite','bisque','darkslategray','blueviolet','fuchsia','darkolivegreen','paleturquoise','aliceblue','lightgoldenrodyellow','rebeccapurple','khaki','peru','moccasin','mediumvioletred']


CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256
root = tk.Tk()
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg='black')

def draw_pixel(i,j,color):
    canvas.create_rectangle(i,j,i,j,outline=color,fill=color)



draw_pixel(128,128,"white")



p1= tk.Button(root,text="aléatoire")
p2= tk.Button(root,text="dégradé")
p3= tk.Button(root,text="dégradé 2D")





p1.grid(row=2,column=1)
p2.grid(row=3,column=1)
p3.grid(row=4,column=1)
canvas.grid(row=2, rowspan=4, column=2)
root.mainloop()