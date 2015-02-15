import static java.lang.System.*;
import java.util.*;
import java.io.*;

public class GA {

	static int popSize = 20;

	Random rand = new Random(50);

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

	public Person[] tournSelect() {
		int[] tourn1 = randShuffle(initializeIndex(popSize));
		int[] tourn2 = randShuffle(initializeIndex(popSize));
		Person[] children = new Person[popSize];
		for (int i = 0; i < popSize; i++) {
			if (pop[tourn1[i]].compareTo(pop[tourn2[i]]) < 1) 
				children[i] = new Person(pop[tourn1[i]].dna, rand);
			else 
				children[i] = new Person(pop[tourn2[i]].dna, rand);
		}

		//do crossover and mutation on children
		for (int i = 0; i < children.length; i += 2) {
			//int ri = rand.next  Int(popSize);
			Person[] coResult = children[i].crossover(children[i+1]);
			coResult[0].mutation();
			coResult[1].mutation();
			children[i] = coResult[0];
			children[i+1] = coResult[1];
		}

		return children;		
	}

	public void mergeAndReduce(Person[] parents, Person[] children) {
		Person[] newPop = new Person[popSize * 2];
		for (int i = 0; i < popSize; i++) {
			newPop[i] = parents[i];
			newPop[i+20] = children[i];
		}
		Arrays.sort(newPop);
		Person[] nextGen = new Person[popSize];
		nextGen[0] = newPop[0];
		nextGen[1] = newPop[1];
		for (int i = 2; i < popSize; i++) {
			nextGen[i] = newPop[rand.nextInt(38) + 2];
		}
		pop = nextGen;
	}

	public void run() throws IOException {

		int runCount = 10;
		for (int run = 0; run < runCount; run++) {
			File file = new File("C:/Users/Abbas/Documents/CIG/outputMat" + run + ".txt");
			file.getParentFile().mkdirs();

			PrintWriter printWriter = new PrintWriter("outputMat"+run+".txt");
			//out.println("run = " + run);
			int totalGen = 200;
			double[] avgX = new double[totalGen];
			double[] bestY = new double[totalGen];
			double[] bestX = new double[totalGen];

			int gen = 0;
			printWriter.print("Gen\tavgX\tbestX\n");
			initializePop();
			do {
				double sum = 0;
				double min = Double.MAX_VALUE;
				for (Person p: pop) {
					double x = p.decode(p.dna);
					sum += x;
					if (p.getFitness() < min) {
						min = x;
						bestY[gen] = p.getFitness();
					}
				}
				avgX[gen] = sum / popSize;
				bestX[gen] = min;
				//out.printf("\tGen %d\tavgX = %.5f\tand bestX is %.5f\tf(x)= %.5f\n", gen, avgX[gen], bestX[gen], bestY[gen]);
				//printWriter.print(gen + "\t" + avgX[gen] + "\t" + bestX);
				printWriter.printf("%d\t%.5f\t%.5f\n", gen, avgX[gen], bestX[gen]);
				/*
				for (int i = 0; i < popSize; i++) {
					out.println(pop[i].getFitness());
				}
				*/
				gen++;

				Person[] children = tournSelect();
				mergeAndReduce(pop, children);

			} while (gen < totalGen);
			printWriter.close();
			/*
			gen--;
			out.printf("\tGen %d\tavgX = %.5f\tand bestX is %.5f\tf(x)= %.5f\n", gen, avgX[gen], bestX[gen], bestY[gen]);
			out.println();
			*/
		}
	}

	public static void main(String[] args) throws IOException{
		new GA().run();		
	}
}