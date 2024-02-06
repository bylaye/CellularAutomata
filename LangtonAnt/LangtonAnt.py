"""
les régles d'application
Les cases d'une grille bidimensionnelle peuvent être blanches ou noires. 
On considère arbitrairement l'une de ces cases comme étant l'emplacement 
initial de la fourmi. Dans l'état initial, toutes les cases sont de la 
même couleur.

La fourmi peut se déplacer à gauche, à droite, en haut ou en bas d'une 
case à chaque fois selon les règles suivantes :

1- Si la fourmi est sur une case noire, elle tourne de 90° vers la gauche, 
change la couleur de la case en blanche et avance d'une case.
  
2- Si la fourmi est sur une case blanche, elle tourne de 90° vers la droite, 
change la couleur de la case en noire et avance d'une case.

"""

BLACK = 'X'
WHITE = ' '

BOTTOM = 'BOTTOM'
TOP = 'TOP'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

class LangtonAnt:

	def __init__(self, max_x = 20, max_y = 20, direction = TOP, initial_state = WHITE):
		self.max_x = max_x
		self.max_y = max_y
		self.state = initial_state
		self.position = (int(max_x/2), int(max_y/2))
		self.direction = direction
		self.cells_grid = [[WHITE]*max_x for _ in range(max_y)]
		self.move_count = 0
		self.initial = None

	def initialise_cells_grid(self, cells, state=BLACK):
		if self.move_count == 0:
			for cell in cells:
				x,y=cell
				self.cells_grid[x][y] = state
			self.initial = {'pos':cells, 'state':state}

	def update_cell_state(self, position):
		x, y = position
		self.cells_grid[x][y] = WHITE if self.cells_grid[x][y] != WHITE else BLACK
		self.state = self.cells_grid[x][y]
	
	def ant_move(self):
		x, y = self.position
		state = self.get_state()
		direction = self.get_direction()
		if self.direction == TOP:
			next_x = x 
			next_y = y+1 if state == WHITE else y-1
			self.direction = RIGHT if next_y > y else LEFT
		elif self.direction == BOTTOM:
			next_x = x 
			next_y = y-1 if state == WHITE else y+1
			self.direction = LEFT if next_y < y else RIGHT
		elif self.direction == LEFT:
			next_y = y 
			next_x = x-1 if state == WHITE else x+1
			self.direction = TOP if next_x < x else BOTTOM
		elif self.direction == RIGHT:
			next_y = y 
			next_x = x+1 if state == WHITE else x-1
			self.direction = BOTTOM if next_x > x else TOP
		self.update_cell_state(self.position)
		self.position = (next_x, next_y)
		self.move_count += 1
		return {
			'pred': ((x,y), direction, self.state),
			'next': (self.position, self.direction, self.cells_grid[next_x][next_y])
			}
		
	def get_max_x(self):
		return self.max_x

	def get_max_y(self):
		return self.max_y
	
	def get_cells_grid(self):
		return self.cells_grid
		
	def get_state(self):
		x, y = self.position
		return self.cells_grid[x][y]
	
	def get_position(self):
		return self.position
	
	def get_direction(self):
		return self.direction
		
	def get_move_count(self):
		return self.move_count
		
	def __str__(self):
		p = ''
		for cells in self.get_cells_grid():
			p += str(cells)+'\n'
		p += 'Initialise position : '+str(self.initial)+'\nmove count : '+ \
			str(self.move_count)+'\ncurrent position :  '+ \
			str(self.position)+' direction : '+str(self.direction)
		return p

