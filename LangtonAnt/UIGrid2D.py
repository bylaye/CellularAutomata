"""
Mode graphic interface of Langton Ant
"""

from tkinter import Tk, Canvas, Button, LEFT, BOTTOM
import LangtonAnt as la

COLOR_BACKGROUND_CANVAS = 'blue'
COLOR_LINE_CELLULE_SEPARATOR = 'black'
COLOR_LIGHT_CELLULE = 'white'
COLOR_DARK_CELLULE = 'black'
COLOR_OUTLINE_NEXT_CELLULE = 'yellow'
COLOR_LABEL_TEXT = 'green'
WIDTH_CELLULE_SEPARATOR = 1

CELLULE_SIZE = 20
MIN_X = 0 #A ne pas changer
MIN_Y = 0 #A ne pas changer
MAX_X = 700
MAX_Y = 700
MAT_X = int(MAX_X / CELLULE_SIZE)
MAT_Y = int(MAX_Y / CELLULE_SIZE)
INTERVAL_SIMULATION = 200 #millisecond unit

root = Tk()
root.title('Max Carrot Rewarded')
canvas = Canvas(root,  width=MAX_X, height=MAX_Y, background=COLOR_BACKGROUND_CANVAS)
#canvas.pack(fill='both', expand=True)

def trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y):
	canvas.create_rectangle(MIN_X, MIN_X, MAX_X, MAX_Y, width=1, fill=COLOR_LIGHT_CELLULE)
	for i in range(MIN_X+CELLULE_SIZE, MAX_X, CELLULE_SIZE):
		canvas.create_line((i, MIN_X, i, MAX_Y), width=WIDTH_CELLULE_SEPARATOR, fill=COLOR_LINE_CELLULE_SEPARATOR)
	for j in range(MIN_Y+CELLULE_SIZE, MAX_Y, CELLULE_SIZE):
		canvas.create_line((MIN_Y, j, MAX_X, j), width=WIDTH_CELLULE_SEPARATOR, fill=COLOR_LINE_CELLULE_SEPARATOR)

langton = la.LangtonAnt(MAT_Y, MAT_X)
#langton.set_direction(la.LEFT)
label_text_id = None # pour effacer le text label apres chaque iteration
def simulation():
    global label_text_id
    move =  langton.ant_move()
    pred = move['pred']
    y,x = pred[0]
    state = pred[2]
    next_cell = move['next']
    y_next,x_next = next_cell[0]
    count = langton.get_move_count()
    text_label = f'Total Move Count = {count}'
    color = COLOR_LIGHT_CELLULE if state != la.WHITE else COLOR_DARK_CELLULE
    r = (x*CELLULE_SIZE, y*CELLULE_SIZE, CELLULE_SIZE*(x+1), CELLULE_SIZE*(y+1))
    r_next = (x_next*CELLULE_SIZE, y_next*CELLULE_SIZE, CELLULE_SIZE*(x_next+1), CELLULE_SIZE*(y_next+1))
    canvas.create_rectangle(r, width = WIDTH_CELLULE_SEPARATOR,outline=COLOR_LINE_CELLULE_SEPARATOR, fill = color)
    canvas.create_rectangle(r_next, width = WIDTH_CELLULE_SEPARATOR, outline = COLOR_OUTLINE_NEXT_CELLULE)
    if label_text_id is not None:
        canvas.delete(label_text_id)
    label_text_id = canvas.create_text(0, 5, text=text_label, font=("Helvetica", 20), anchor="nw", fill=COLOR_LABEL_TEXT)
    root.after(INTERVAL_SIMULATION, simulation)

def play():
	simulation()

def run():
    trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y)
    start_simulation = Button(root, text='START SIMULATION', width=20, command=play)
    start_simulation.pack(side=BOTTOM, padx=10, pady=20)
    canvas.pack(expand=False)
    root.mainloop()

run()
