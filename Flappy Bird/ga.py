import random, math

from braindna import dna 

population = []
pop_size = 200
generations = 50

# Create initial population 
for x in range(pop_size):
 	population.append( dna() )

best=None
for generation in range(generations):
	 for individual in population:
	  	individual.evaluate()

	 population.sort(key=lambda x:x.fitness,reverse=True) 
	 population=population[0:pop_size/2] #keep top 50% of population, discard the rest
	 best=population[0]
	 print generation, population[0].fitness

	 new_population = [best]
	 for x in range(1,pop_size):

		  if random.random()<0.5: # randomly pick a member of population, mutate, and add to new pop
			   child=random.choice(population).mutate()
			   new_population.append(child)

		  else: #pick two random parents, perform crossover, and add child to population
			   p1 = random.choice(population)
			   p2 = random.choice(population)
			   child=p1.crossover(p2)
			   new_population.append(child)

	 population=new_population


from test import game
ann=best.create_neuron()
print game(ann,True) #Get best neuron and show it playing the game