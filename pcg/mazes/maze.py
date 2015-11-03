import random, math

global func
global crossoverRate
global mutationRate
global solvable
global pop

def setPop(p):
    global pop
    pop = p

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

# uses binary encoding
# for sure has open entering
def initPop(size, len):
    pop = []
    for i in range(size):
        indiv = "0"
        for i in range(len-2):
            indiv += str(random.randint(0,1))
        indiv += "0"
        pop.append(indiv)
    return pop

# converts to maze using binary
def phenotypeArr(ind1):
    rows = 8
    maze = []
    for i in range(len(ind1)/rows):
        a = ind1[i*8:(i+1)*8]
        maze.append([])
        maze[i] = list(a)
    #print maze
    return maze


# TODO: define fitnesses
def fitness(ind):
    global func
    global pop
    a = func(ind, pop)
    print 'fit: ' + str(a)

def normalFitness(ind, pop):
    score = complexScore(ind)
    if isSolvable(ind):
        return score*10
    return score*10 + 500

def randomFitness(ind, pop):
    return random.randint(0,64)

def noveltyFitness(ind, pop):
    diff = 0
    for i in range(len(pop)):
        if ind is not pop[i]:
            diff -= numDiff(ind, pop[i])
    fit = diff/float(len(pop))
    if (isSolvable(ind)):
        fit -= 500
    return fit

def numDiff(ind1, ind2):
    count = 0;
    for i in range(len(ind1)):
        if ind1[i] is ind2[i]:
            count += 1
    return count

def sumFit(pop):
    sum = 0
    for i in range(len(pop)):
        fit = func(pop[i], pop)
        sum += fit
    return sum

def sumComp(pop):
    sum = 0
    for i in range(len(pop)):
        score = complexScore(pop[i])
        sum += score
    return sum

def numOnes(ind):
    count = 0
    for i in range(len(ind)):
        if ind[i] is '1':
            count += 1
    return count

def complexScore(ind):
    return abs(numOnes(ind) - 27)

def isSolvable(maze):
    global solvable
    resetSolvable()
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
    global pop
    return int(func(ind1, pop) - func(ind2, pop))

def compareFit(ind1, ind2):
    global func
    global pop
    if func(ind1, pop) < func(ind2, pop):
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
        num = random.randint(0,1)
        ind1 = ind1[:index] + str(num) + ind1[index+1:]
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
