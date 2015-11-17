# Flappy Bird AI
## Created using neuroevolution

To run the neuroevolution, just pull the files and run ga.py with python
To play, run play.py with python

## Test Info

### Genetic Algorithm 
Population Size: 200
Generations: 50

### Neural Network
Inputs: 4
	- euclidean distance b/w top pillar and bird
	- euclidean distance b/w bottom pillar and bird
	- wait time till next command can be executed
	- 1.0

Outputs: 1
	- Whether bird goes up or doesn't move

