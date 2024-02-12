
PATTERN = '111  110  101  100  011  010  001  000'

"""convert int value to binary format 8 bits"""
def int_to_bin_8bits(number):
    number = int(number)
    r = [2**i for i in range(7, -1, -1)]
    out = ''
    for c in r:
        if number >= c:
            number %= c
            out += '1'
        else:
            out += '0'
    return out


class SimpleCellular:

    def __init__(self, rule=0, 
            pattern_initial=PATTERN, 
            max_x=20, max_y=20, state_0=0, state_1=1 
            ):
        self.rule = rule
        self.pattern_initial = pattern_initial
        self.max_x = max_x
        self.max_y = max_y
        self.state_1 = state_1
        self.state_0 = state_0
        self.plateau = [[state_0]*max_y for _ in range(max_x)]
        self.rules_pattern = self.rules()
        self.plateau[0][int(max_y/2)] = state_1
        self.next_line = 1
        
    def get_plateau(self):
        return self.plateau

    def __str__(self):
        out = ''
        for i in range(self.next_line):
            p = self.plateau[i]
            out += ''.join(p)+'\n'
        return out
 
    def get_state_0(self):
       return self.state_0

    def get_state_1(self):
       return self.state_1

    """ dictionnaire de correspondance motif initial : rule"""
    def rules(self):
        pattern_initial_list = self.pattern_initial.split()
        rule_in_8bits = int_to_bin_8bits(self.rule)
        return {pattern_initial_list[i]:int(rule_in_8bits[i]) for i in range(8)}
    
    """ conversion des valeurs des etats en binaire 0 ou 1"""
    def convert_state(self, triplet):
        new_triplet = ''
        for t in triplet:
            new_triplet += '1' if t == self.state_1 else '0'
        return self.state_1 if self.rules_pattern[new_triplet] == 1 else self.state_0
    
    """ etat t+1 de la cellule a totalement a gauche qui n'a pas de voisine gauche"""
    def next_extreme_left(self,n):
        l1 = self.plateau[n-1][0]
        l2 = str(self.plateau[n-1][1])
        l3 = str(self.plateau[n-1][2])
        triplet = l1+l2+l3
        self.plateau[n][0] = self.convert_state(triplet)

    """ etat t+1 de la cellule a totalement a droite qui n'a pas de voisine droite"""
    def next_extreme_right(self,n):
        y = self.max_y
        l1 = self.plateau[n-1][y-1]
        l2 = str(self.plateau[n-1][y-2])
        l3 = str(self.plateau[n-1][y-3])
        triplet = l1+l2+l3
        self.plateau[n][y-1] = self.convert_state(triplet)

    """ etat t+1 des cellules avec des voisines gauche et droite"""
    def next_step(self, n):
        rules = self.rules()
        for i in range(1,self.max_y-1):
            left = str(self.plateau[n-1][i-1])
            right = str(self.plateau[n-1][i+1])
            current = str(self.plateau[n-1][i])
            triplet = left+current+right
            self.plateau[n][i] = self.convert_state(triplet)
    
    """ Mise a jour des cellules t+1"""
    def update(self):
        if self.next_line < self.max_x:
            self.next_extreme_left(self.next_line)
            self.next_step(self.next_line)
            self.next_extreme_right(self.next_line)
            self.next_line += 1
