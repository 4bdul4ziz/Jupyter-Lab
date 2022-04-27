import numpy as np

class board:
    def __init__(self):
        g = [None]*3
        self.g = np.array([[0]*3 for _ in g])
        self.isEmpty = set([(i,j) for i in range(3) for j in range(3)])
    def add(self, pos, player):
        self.g[pos] = player
        self.isEmpty.remove(pos)
    def remove(self, pos):
        self.g[pos] = 0
        self.isEmpty.add(pos)

def draw(g, width=7, height=5):
    lempty = '|'.join([' '*width]*3) + "\n"
    hbar = '+'.join(['-'*width]*3) + "\n"
    def line(r):
        emp2 = ' '*(width//2)
        return '|'.join([emp2+x+emp2 for x in r])+"\n"
    def emp(i):
        i = 2 - i
        return '|'.join([' '*(width-1)+str(i*3+j+1)
                         for j in range(3)]) + "\n"
    return hbar.join(lempty*(height//2) + line(x) +
                     lempty*(height//2-1) + emp(i)
                     for i,x in enumerate(g))



def draw_ch_map(g):
    ch_map = {0: ' ', 1: 'X', -1: 'O'}
    print(draw([map(lambda y: ch_map[y], x) for x in g]))

def get_input(prompt,choices):
    while True:
        print(prompt+":")
        i = input()
        if i in choices:
            return i

def score_board(g):
    s = len(g)
    rs = range(s)
    for i in rs:
        # row win
        if (g[i,0] != 0 and
            all(g[i,j] == g[i,(j+1)%s] for j in rs)):
            return g[i,0] == 1 and 100 or -100
        # col win
        if (g[(0,i)] != 0 and
            all(g[j,i] == g[(j+1)%s,i] for j in rs)):
            return g[0,i] == 1 and 100 or -100
    # dia win
    if (g[0,0] != 0 and
        all(g[i,i] == g[(i+1)%s,(i+1)%s] for i in rs)):
        return g[0,0] == 1 and 100 or -100
    if (g[0,s-1] != 0 and
        all(g[i,s-i-1] == g[(i+1)%s,s-((i+1)%s)-1] for i in rs)):
        return g[0,s-1] == 1 and 100 or -100
    return 0

def minmax(b, depth, player):
    def comp(player):
        if player == 1:
            return lambda x,y: x > y
        else:
            return lambda x,y: x < y
    gt = comp(player)

    move = None
    score = score_board(b.g)
    if score == 100:
        return score, move
    if score == -100:
        return score, move
    if len(b.isEmpty) == 0:
        return 0, move

    best = -player*1000
    g = b.isEmpty.copy()
    for pos in g:
        b.add(pos,player)
        score, amove = minmax(b, depth+1, -player)
        if gt(score, best):
            best = score
            move = pos
        b.remove(pos)
    return best, move

def check_score(b):
    if score_board(b.g) == -100:
        print("You win")
        return True
    if score_board(b.g) == 100:
        print("I win")
        return True
    if len(b.isEmpty) == 0:
        print("Tie")
        return True
    return False

def main(computer_starting_pos=(2,0)):
    """ play against computer """
    b = board()
    def pos(i):
        return (9-i) // 3, (i-1) % 3
    if get_input("Computer first [y/n]",'yn') == 'y':
        b.add(computer_starting_pos, 1)
        draw_ch_map(b.g)
    while True:
        valid = False
        while not valid:
            i = int(get_input('Move [1-9]','123456789'))
            if b.g[pos(i)] == 0:
                b.add(pos(i), -1)
                valid = True
        draw_ch_map(b.g)
        if check_score(b):
            break
        best, move = minmax(b, 0, 1)
        b.add(move, 1)
        draw_ch_map(b.g)
        if check_score(b):
            break

main(computer_starting_pos=(1,1))