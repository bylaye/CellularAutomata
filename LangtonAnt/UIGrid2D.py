

from tkinter import Tk, Canvas, Button, LEFT, BOTTOM
import LangtonAnt as la

COLOR_BACKGROUND_CANVAS = 'blue'
LINE_CELLULE_SEPARATOR = 'black'
WIDTH_CELLULE_SEPARATOR = 2
COLOR_OUTLINE_START_CELLULE = 'yellow'
COLOR_LIGHT_CELLULE = 'black'
COLOR_DARK_CELLULE = 'red'

CELLULE_SIZE = 5
MIN_X = 0 #A ne pas changer
MIN_Y = 0 #A ne pas changer
#MAX_X = MAT_X * CELLULE_SIZE
#MAX_Y = MAT_Y * CELLULE_SIZE
MAX_X = 600
MAX_Y = 500
MAT_X = int(MAX_X / CELLULE_SIZE)
MAT_Y = int(MAX_Y / CELLULE_SIZE)

root = Tk()
root.title('Max Carrot Rewarded')
canvas = Canvas(root,  width=MAX_X, height=MAX_Y+0, background=COLOR_BACKGROUND_CANVAS)
#canvas.pack(fill='both', expand=True)

def trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y):
	canvas.create_rectangle(MIN_X, MIN_X, MAX_X, MAX_Y, width=1, fill=COLOR_LIGHT_CELLULE)
	for i in range(MIN_X+CELLULE_SIZE, MAX_X, CELLULE_SIZE):
		canvas.create_line((i, MIN_X, i, MAX_Y), width=WIDTH_CELLULE_SEPARATOR, fill=LINE_CELLULE_SEPARATOR)
	for j in range(MIN_Y+CELLULE_SIZE, MAX_Y, CELLULE_SIZE):
		canvas.create_line((MIN_Y, j, MAX_X, j), width=WIDTH_CELLULE_SEPARATOR, fill=LINE_CELLULE_SEPARATOR)

langton = la.LangtonAnt(MAT_Y, MAT_X)
langton.set_direction(la.LEFT)
def simulation():
    move =  langton.ant_move()
    pred = move['pred']
    y,x = pred[0]
    state = pred[2]
    print(langton.get_move_count())
    color = COLOR_LIGHT_CELLULE if state != la.WHITE else COLOR_DARK_CELLULE
    r = (x*CELLULE_SIZE, y*CELLULE_SIZE, CELLULE_SIZE*(x+1), CELLULE_SIZE*(y+1))
    canvas.create_rectangle(r, fill = color)
    root.after(3, simulation)

def play():
	simulation()

def run():
    trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y)
    start_simulation = Button(root, text='START SIMULATION', width=20, command=play)
    start_simulation.pack(side=BOTTOM, padx=10, pady=20)
    canvas.pack(expand=False)
    root.mainloop()

run()
