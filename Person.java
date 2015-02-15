import java.util.*;

public class Person implements Comparable<Person> {
	
	final int bits;
	final int min;
	final int max;
	final double pCross = .9;
	final double pMut = .05;

	int[] dna;

	Random rand;

	public Person(Random rand) {
		this(20, 0, 1, rand);
	}

	public Person(int[] dna, Random rand) {
		this(rand);
		this.dna = dna;
	}

	public Person(int bits, int min, int max, Random rand) {
		this.bits = bits;
		this.min = min;
		this.max = max;
		//rand = new Random(1);
		dna = new int[bits];
		this.rand = rand;
		initializeDNA();
	}

	public int getBit(int index) {
		return dna[index];
	}

	public void setBit(int index, int i) {
		dna[index] = i;
	}

	void initializeDNA() {
		for (int i = 0; i < dna.length; i++) {
			dna[i] = rand.nextInt(2);
		}
	}

	public int evalDNA(int[] dna) {
		String s = "";
		for (int i: dna) {
			s += i+"";
		}

		return Integer.parseInt(s, 2);
	}

	public double decode(int[] dna) {
		int s = evalDNA(dna);
		double x = min + (max - min) * s / (Math.pow(2, bits) - 1);
		return x;
	}

	public double evalFitness(double x) {
		return Math.pow((6 * x - 2), 2) * Math.sin(12 * x - 4);
	}

	public int[] crossoverAndMutation(Person p2) {
		int[] dnaCopy = Arrays.copyOf(dna, dna.length);
		if (rand.nextDouble() < pCross) {
			int singlePt = rand.nextInt(bits);
			for (int i = singlePt; i < bits; i++) {
				dnaCopy[i] = p2.dna[i];
			}
		}
		for (int i = 0; i < bits; i++) {
			if (rand.nextDouble() < pMut) {
				dnaCopy[i] = (i+1) % 2;
			}
		}
		return dnaCopy;
	}

	public int compareTo(Person p) {
		double p1 = evalFitness(decode(dna));
		double p2 = evalFitness(decode(p.dna));
		if (p1 < p2) return -1;
		if (p1 > p2) return 1;
		return 0;
	} 

	public String toString() {
		return Arrays.toString(dna);
	}

}