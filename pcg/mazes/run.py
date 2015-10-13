from maze import *

def printMaze(ind):
    maze = phenotypeArr(ind)
    for i in range(len(maze)):
        row = ""
        for j in range(len(maze[i])):
            row += maze[i][j]
        print row

def numSolvable(pop):
    count = 0
    for i in range(len(pop)):
        resetSolvable()
        if isSolvable(pop[i]):
            count += 1
    return count

def printSolvable(pop):
    for i in range(len(pop)):
        resetSolvable()
        if isSolvable(pop[i]):
            printMaze(pop[i])
            print''
# main

setCrossoverRate(0.9)
setMutationRate(0.1)
popSize = 20
arraySize = 64
generations = 10;

setFunc(normalFitness)
resetSolvable()

pop = initPop(popSize,arraySize*2)
print(numSolvable(pop))

for i in range(generations):
    avgFitness = sumFit(pop)/float(len(pop))
    avgComplexity = sumComp(pop)/float(len(pop))
    print (str(i) + ' avg fitness:\t' + str(avgFitness))
    print (str(i) + ' avg complexity:\t' + str(avgComplexity))
    #print ('numSolvable:\t' + str(numSolvable(pop)))
    print ''
    children = tournSelect(pop)
    children = crossAndMut(children)
    pop = newPop(pop, children)

print(numSolvable(pop))
printSolvable(pop)
print len(pop)









