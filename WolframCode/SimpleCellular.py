
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
        self.plateau[0][int(max_y/2)] = state_1

    def get_plateau(self):
        return self.plateau

    def __str__(self):
        out = ''
        for p in self.plateau:
            out += str(p)+'\n'
        return out

    def rules(self):
        pattern_initial_list = self.pattern_initial.split()
        rule_in_8bits = int_to_bin_8bits(self.rule)
        return {pattern_initial_list[i]:int(rule_in_8bits[i]) for i in range(8)} 
