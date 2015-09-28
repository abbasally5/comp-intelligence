import random, math

global func
global crossoverRate
global mutationRate
global solvable

def setFunc(fit):
    global func
    func = fit

def setCrossoverRate(num):
    global crossoverRate
    crossoverRate = num

def setMutationRate(num):
    global mutationRate
    mutationRate = num

def resetSolvable():
    global solvable
    solvable = False

def initPop(size, len):
    pop = []
    for i in range(size):
        indiv = ""
        for i in range(len):
            hexNum = hex(random.randint(0,15))
            indiv += hexNum[2:]
        pop.append(indiv)
    return pop

# hex to binary string
def phenotype(ind1):
    numlen = len(ind1) * math.log(16, 2) # num of chars in ind1 * 4
    num = bin(int(ind1, 16))
    return num[2:].zfill(int(numlen))

# converts to actual maze
def phenotypeArr(ind1):
    s = phenotype(ind1)
    maze = []
    #'''
    for i in range((len(ind1)/2)):
        a = s[i*8:(i+1)*8]
        maze.append([])
        maze[i] = list(a)
    #'''
    '''
    for i in range((len(ind1)/2)):
        for j in range((len(ind1)/2)):
            char = s[i*(len(ind1)/2) + j]
            maze[i][j] = char
    '''
    return maze

# TODO: define fitnesses
def fitness(ind):
    global func
    a = func(ind)
    print 'fit: ' + str(a)

def normalFitness(ind):
    pass

def randomFitness(ind):
    return random.randint(0,64)

def noveltyFitness(ind):
    pass

def sumFit(pop):
    sum = 0
    for i in range(len(pop)):
        sum += func(pop[i])
    return sum

def isComplex():
    pass

def isSolvable(maze):
    global solvable
    solve(0,0, phenotypeArr(maze))
    return solvable

def solve(x, y, maze):
    global solvable
    if (x is 7 and y is 8):
        solvable = True
        return
    if (x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] is '1'):
        return
    maze[x] = setStr(x,y, maze, '1')
    solve(x, y+1, maze)
    solve(x, y-1, maze)
    solve(x+1, y, maze)
    solve(x-1, y, maze)
    maze[x] = setStr(x,y, maze, '0')
    return

def setStr(x,y, arr, str):
    l1 = list(arr[x])
    l1[y] = str
    return ''.join(l1)

def tournSelect(pop):
    winners = []
    for num in range(2):
        indices = randShuffle(initIndices(len(pop)))
        i = 0
        while i < len(pop)-2:
            winners.append(compareFit(pop[indices[i]], pop[indices[i+1]]))
            i += 2
    return winners

def initIndices(size):
    indices = []
    for i in range(0,size-1):
        indices.append(i)
    return indices

def randShuffle(indices):
    i = len(indices) - 1
    while (i > 0):
        rand = random.randint(0,i)
        temp = indices[rand];
        indices[rand] = indices[i]
        indices[i] = temp
        i -= 1
    return indices

def compare(ind1, ind2):
    global func
    return func(ind1) - func(ind2)

def compareFit(ind1, ind2):
    global func
    if func(ind1) < func(ind2):
        return ind1
    return ind2

def newPop(pop1, pop2):
    nextGen = []
    top = 2
    totalPop = pop1 + pop2
    totalPop = sorted(totalPop, cmp=compare)
    for i in range(top):
        nextGen.append(totalPop[i])
    for i in range(len(pop1) - top):
        nextGen.append(totalPop.pop(random.randint(top,len(totalPop)-1)))
    return nextGen

def mutation(ind1):
    if random.random() < mutationRate:
        index = random.randint(0, len(ind1)-1)
        hexNum = hex(random.randint(0,15))
        ind1 = ind1[:index] + hexNum[2:] + ind1[index+1:]
    return ind1

def crossover(ind1, ind2):
    if random.random() < crossoverRate:
        index = random.randint(0,len(ind1)-1)
        temp = ind1[index:]
        ind1 = ind1[:index] + ind2[index:]
        ind2 = ind2[:index] + temp
    return ind1, ind2

def crossAndMut(pop):
    i = 0
    while i < len(pop):
        pop[i], pop[i+1] = crossover(pop[i], pop[i+1])
        pop[i] = mutation(pop[i])
        pop[i+1] = mutation(pop[i+1])
        i += 2
    return pop
