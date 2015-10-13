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

setFunc(normalFitness)
resetSolvable()

pop = initPop(popSize,arraySize*2)

for i in range(generations):
    avgFitness = sumFit(pop)/float(len(pop))
    avgComplexity = sumComp(pop)/float(len(pop))
    print ('avg fitness:\t' + str(avgFitness))
    print ('avg complexity:\t' + str(avgComplexity))
    children = tournSelect(pop)
    children = crossAndMut(children)
    pop = newPop(pop, children)

count = 0
for i in range(len(pop)):
    resetSolvable()
    if isSolvable(pop[i]):
        count += 1
        printMaze(pop[i])
        print''
print count
print len(pop)









