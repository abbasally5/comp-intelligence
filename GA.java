import static java.lang.System.*;
import java.util.*;

public class GA {

	static int popSize = 20;

	Random rand = new Random(1);

	Person[] pop;

	public void initializePop() {
		pop = new Person[popSize];

		for (int i = 0; i < pop.length; i++ ) {
			pop[i] = new Person(rand);
		}
	}

	public int[] initializeIndex(int popSize) {
		int[] ind = new int[popSize];
		for (int i = 0; i < popSize; i++) {
			ind[i] = i;
		}
		return ind;
	}

	public int[] randShuffle(int[] ind) {
		//uses fisher-yates shuffle method
		for (int i = ind.length - 1; i > 0; i--) {
			int randNum = rand.nextInt(i+1);
			//swap with random index
			int placeholder = ind[randNum];
			ind[randNum] = ind[i];
			ind[i] = placeholder;
		}
		return ind;
	}

	//returns 5 people for reproduction for next gen
	public Person[] tournSelect() {
		
		int[] tourn1 = randShuffle(initializeIndex(popSize));
		Person[] parents = new Person[5];
		for (int i = 0; i < parents.length; i ++) {
			Person[] group = new Person[4]; //popSize / 5
			for (int j = 0; j < group.length; j++)
			{
				group[j] = pop[tourn1[i*4+j]];
			}
			Arrays.sort(group);
			parents[i] = group[0];
		}
		return parents;
		
		/*
		// Method 2
		int[] tourn1 = randShuffle(initializeIndex(popSize));
		int[] tourn2 = randShuffle(initializeIndex(popSize));
		Person[] nextGen = new Person[popSize];
		for (int i = 0; i < popSize; i++) {
			if (pop[tourn1[i]].compareTo(pop[tourn2[i]]) < 1) 
				nextGen[i] = pop[tourn1[i]];
			else 
				nextGen[i] = pop[tourn2[i]];
		}
		for (int i = 0; i < popSize; i++) {

		}
		*/
	}

	public void nextGen(Person[] parents) {
		Person[] nextGen = new Person[popSize];
		for(int i = 0; i < popSize; i++) {
			for (int j = 0; j < parents.length; j++ ) {
				if (i/5 != j){
					nextGen[i] = new Person(parents[i/5].crossoverAndMutation(parents[j]), rand);
				}
			}
		}
		pop = nextGen;
	}

	public void run() {
		int runCount = 10;
		for (int run = 0; run < runCount; run++) {
			out.println("run = " + run);
			int totalGen = 200;
			double[] avgFit = new double[totalGen];
			double[] bestFit = new double[totalGen];
			double[] bestX = new double[totalGen];

			int gen = 0;
			initializePop();
			do {
				double sum = 0;
				double min = Double.MAX_VALUE;
				for (Person p: pop) {
					double fitness = p.evalFitness(p.decode(p.dna));
					sum += fitness;
					if (fitness < min) {
						min = fitness;
						bestX[gen] = p.decode(p.dna);
					}
				}
				avgFit[gen] = sum / popSize;
				bestFit[gen] = min;
				out.printf("\tGen %d\tavgFit = %.5f\tand bestFit is %.5f\n", gen, avgFit[gen], bestFit[gen]);
				gen++;

				Person[] parents = tournSelect();
				nextGen(parents);

			} while (gen < totalGen);
			out.println();
		}
	}

	public static void main(String[] args) {
		new GA().run();		
	}
}