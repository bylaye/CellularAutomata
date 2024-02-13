"""
Mode interface graphique
"""

from tkinter import Tk, Canvas, Button, LEFT, BOTTOM
from SimpleCellular import SimpleCellular

COLOR_BACKGROUND_CANVAS = 'blue'
COLOR_LINE_CELLULE_SEPARATOR = 'black'
COLOR_LIGHT_CELLULE = 'white'
COLOR_DARK_CELLULE = 'black'
COLOR_OUTLINE_NEXT_CELLULE = 'yellow'
COLOR_LABEL_TEXT = 'green'
WIDTH_CELLULE_SEPARATOR = 1

CELLULE_SIZE = 2
MIN_X = 0 #A ne pas changer
MIN_Y = 0 #A ne pas changer
MAX_X = 1200
MAX_Y = 700
MAT_X = int(MAX_X / CELLULE_SIZE)
MAT_Y = int(MAX_Y / CELLULE_SIZE)
INTERVAL_SIMULATION = 20 #millisecond unit

root = Tk()
root.title('Simple Cellular code de wolfram 2^8')
canvas = Canvas(root,  width=MAX_X, height=MAX_Y, background=COLOR_BACKGROUND_CANVAS)
#canvas.pack(fill='both', expand=True)

def trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y):
	canvas.create_rectangle(MIN_X, MIN_X, MAX_X, MAX_Y, width=1, fill=COLOR_LIGHT_CELLULE)
	for i in range(MIN_X+CELLULE_SIZE, MAX_X, CELLULE_SIZE):
		canvas.create_line((i, MIN_X, i, MAX_Y), width=WIDTH_CELLULE_SEPARATOR, fill=COLOR_LIGHT_CELLULE)
	for j in range(MIN_Y+CELLULE_SIZE, MAX_Y, CELLULE_SIZE):
		#canvas.create_line((MIN_Y, j, MAX_X, j), width=WIDTH_CELLULE_SEPARATOR, fill=COLOR_LINE_CELLULE_SEPARATOR)
		canvas.create_line((MIN_Y, j, MAX_X, j), width=WIDTH_CELLULE_SEPARATOR, fill=COLOR_LIGHT_CELLULE)

sc = SimpleCellular(rule=101, state_1=1, state_0= 0, max_x= MAT_Y, max_y=MAT_X)

def imprime(n):
    for y in range(MAT_X):
        color = COLOR_LIGHT_CELLULE if sc.plateau[n][y] == sc.get_state_0() else COLOR_DARK_CELLULE
        r = (y*CELLULE_SIZE, n*CELLULE_SIZE, CELLULE_SIZE*(y+1), CELLULE_SIZE*(n+1))
        canvas.create_rectangle(r, fill = color, outline=COLOR_LIGHT_CELLULE)

iteration = 0
def simulation():
    global iteration
    if iteration < MAT_Y-1:
        imprime(iteration)
        sc.update()
        iteration = sc.next_line - 1
        print(iteration, MAT_X, MAT_Y)
        root.after(INTERVAL_SIMULATION, simulation)
"""
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
    canvas.create_rectangle(r, width = WIDTH_CELLULE_SEPARATOR,outline=COLOR_LINE_CELLULE_SEPARATOR, fill = color)
    root.after(INTERVAL_SIMULATION, simulation)
"""

def play():
	simulation()

def run():
    trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y)
    start_simulation = Button(root, text='START SIMULATION', width=20, command=play)
    start_simulation.pack(side=BOTTOM, padx=10, pady=20)
    canvas.pack(expand=False)
    root.mainloop()

run()
