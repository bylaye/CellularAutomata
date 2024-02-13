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

CELLULE_SIZE = 4
MIN_X = 0 #A ne pas changer
MIN_Y = 0 #A ne pas changer
MAX_X = 1200
MAX_Y = 600
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

RULE=133
#sc = SimpleCellular(rule=RULE, state_1='1', state_0= '0', max_x= MAT_Y, max_y=MAT_X)

def imprime(n):
    for y in range(MAT_X):
        color = COLOR_LIGHT_CELLULE if sc.plateau[n][y] == sc.get_state_0() else COLOR_DARK_CELLULE
        r = (y*CELLULE_SIZE, n*CELLULE_SIZE, CELLULE_SIZE*(y+1), CELLULE_SIZE*(n+1))
        canvas.create_rectangle(r, fill = color, outline=COLOR_LIGHT_CELLULE)

iteration = 0
def simulation():
    global iteration
    if iteration == 0:
        imprime(0)
        iteration += 1
    elif iteration < MAT_Y:
        sc.update()
        imprime(iteration)
        iteration = sc.next_line
        print(f'Rule = {RULE} iteration : {iteration}, Y= {MAT_Y}',end='\r')
        root.after(INTERVAL_SIMULATION, simulation)

def play():
	simulation()

def run():
    trace_cellule(CELLULE_SIZE, MIN_X, MAX_X, MIN_Y, MAX_Y)
    start_simulation = Button(root, text='START SIMULATION', width=20, command=play)
    start_simulation.pack(side=BOTTOM, padx=5, pady=5)
    canvas.pack(expand=False)
    root.mainloop()

if __name__ == '__main__':
    import sys
    print(sys.argv[0], sys.argv[1])
    if len(sys.argv) == 2:
        rule = int(sys.argv[1])
        if rule >= 0 and rule < 256:
            rule = rule
    else:
        rule = RULE
    sc = SimpleCellular(rule=rule, state_1='1', state_0= '0', max_x= MAT_Y, max_y=MAT_X)
    print(f'Start rule = {RULE}')
    run()
