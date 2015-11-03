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
testRuns = 20

'''
setFunc(normalFitness)
resetSolvable()

pop = initPop(popSize,arraySize)
setPop(pop)
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
    setPop(pop)

printSolvable(pop)
print(numSolvable(pop))
print len(pop)
printMaze(pop[i])
'''

# testing - get stats
random.seed(0)
avgInitSolvable = 0
avgSolvable = 0
avgComplexity = 0

print 'Random Fitness'
setFunc(randomFitness)

for i in range(testRuns):
    resetSolvable()

    pop = initPop(popSize, arraySize)
    setPop(pop)
    avgInitSolvable += numSolvable(pop)
    for j in range(generations):
       '''
        if i is 0:
            print j
            printMaze(pop[i])
            print''
        '''
        children = tournSelect(pop)
        children = crossAndMut(children)
        pop = newPop(pop, children)
        setPop(pop)

    avgSolvable += numSolvable(pop)
    avgComplexity += sumComp(pop)/float(len(pop))

avgInitSolvable = avgInitSolvable/float(testRuns)
avgSolvable = avgSolvable/float(testRuns)
avgComplexity = avgComplexity/float(testRuns)
print 'avgInitSolvable:\t' + str(avgInitSolvable) + '\n' + \
      'avgSolvable:\t\t' + str(avgSolvable) + '\n' + \
      'avgComplexity:\t\t' + str(avgComplexity)

random.seed(0)
avgInitSolvable = 0
avgSolvable = 0
avgComplexity = 0

print 'Normal Fitness'
setFunc(normalFitness)

for i in range(testRuns):
    resetSolvable()

    pop = initPop(popSize, arraySize)
    setPop(pop)
    avgInitSolvable += numSolvable(pop)

    for j in range(generations):
        
        children = tournSelect(pop)
        children = crossAndMut(children)
        pop = newPop(pop, children)
        setPop(pop)

    avgSolvable += numSolvable(pop)
    avgComplexity += sumComp(pop)/float(len(pop))

avgInitSolvable = avgInitSolvable/float(testRuns)
avgSolvable = avgSolvable/float(testRuns)
avgComplexity = avgComplexity/float(testRuns)
print 'avgInitSolvable:\t' + str(avgInitSolvable) + '\n' + \
      'avgSolvable:\t\t' + str(avgSolvable) + '\n' + \
      'avgComplexity:\t\t' + str(avgComplexity)

random.seed(0)
avgInitSolvable = 0
avgSolvable = 0
avgComplexity = 0

print 'Novelty Fitness'
setFunc(noveltyFitness)

for i in range(testRuns):
    resetSolvable()

    pop = initPop(popSize, arraySize)
    setPop(pop)
    avgInitSolvable += numSolvable(pop)

    for j in range(generations):
        
        children = tournSelect(pop)
        children = crossAndMut(children)
        pop = newPop(pop, children)
        setPop(pop)

    avgSolvable += numSolvable(pop)
    avgComplexity += sumComp(pop)/float(len(pop))



avgInitSolvable = avgInitSolvable/float(testRuns)
avgSolvable = avgSolvable/float(testRuns)
avgComplexity = avgComplexity/float(testRuns)
print 'avgInitSolvable:\t' + str(avgInitSolvable) + '\n' + \
      'avgSolvable:\t\t' + str(avgSolvable) + '\n' + \
      'avgComplexity:\t\t' + str(avgComplexity)










