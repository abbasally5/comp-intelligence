from maze import *

def printMaze(ind):
    maze = phenotypeArr(ind)
    for i in range(len(maze)):
        print maze[i]


# main

setCrossoverRate(0.9)
setMutationRate(0.1)
popSize = 20
arraySize = 8
generations = 20;

setFunc(randomFitness)

pop = initPop(popSize,arraySize*2)

for i in range(generations):
    avgFitness = sumFit(pop)/float(len(pop))
    print ('avg fitness: ' + str(avgFitness))
    children = tournSelect(pop)
    children = crossAndMut(children)
    pop = newPop(pop, children)

count = 0
for i in range(len(pop)):
    resetSolvable()
    if isSolvable(pop[i]):
        count += 1
        printMaze(pop[i])
print count







