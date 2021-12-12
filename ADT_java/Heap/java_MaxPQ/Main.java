import java.util.*;

public class Main {
	public static void main(String args[]) {
		String[] a = {"S","O","R","T","E","X","A","M"};

		MaxPQ<String> pq = new MaxPQ<String>(a);
		pq.insert("P");
		pq.insert("L");
		pq.insert("E");

		System.out.println("(" + pq.size() + " left on pq)");
		System.out.println(pq.max());
		System.out.println("(" + pq.size() + " left on pq)");
		System.out.println(pq.delMax());
		System.out.println("(" + pq.size() + " left on pq)");
		System.out.println(pq.delMax());
		System.out.println("(" + pq.size() + " left on pq)");
	}
}

class MaxPQ<Key extends Comparable<Key>> {
	private Key[] pq;                    // store items at indices 1 to n
	private int n;                       // number of items on priority queue

	public MaxPQ(int initCapacity) {
		pq = (Key[]) new Comparable[initCapacity + 1];
		n = 0;
	}

	public MaxPQ() {
		this(1);
	}

	public MaxPQ(Key[] keys) {
		n = keys.length;
		pq = (Key[]) new Comparable[keys.length + 1];
		for(int i = 0; i < n; i++)
			pq[i+1] = keys[i];
		for (int k = n/2; k >= 1; k--)
			sink(k);
	}

	public boolean isEmpty() {
		return n == 0;
	}

	public int size() {
		return n;
	}

	public Key max() {
		if (isEmpty()) throw new NoSuchElementException("Priority queue underflow");
		return pq[1];
	}

	// helper function to double the size of the heap array
	private void resize(int capacity) {
		Key[] temp = (Key[]) new Comparable[capacity];

		for(int i = 1; i <= n; i++)
			temp[i] = pq[i];

		pq = temp;
	}

	public void insert(Key x) {
		if (n == pq.length - 1) resize(2 * pq.length);

		// add x, and percolate it up to maintain heap invariant
		pq[++n] = x;
		swim(n);
	}

	public Key delMax() {
		if (isEmpty()) throw new NoSuchElementException("Priority queue underflow");

		Key max = pq[1];
		exch(1, n--);
		sink(1);
		pq[n+1] = null;

		if ((n > 0) && (n == (pq.length - 1) / 4))
			resize(pq.length / 2);

		return max;
	}

	// helper functions

	private void swim(int k) {
		while (k > 1 && less(k/2, k)) {
			exch(k, k/2);
			k = k/2;
		}
	}

	private void sink(int k) {
		while (2 * k <= n) {
			int j = 2*k;
			if (j < n && less(j, j+1)) j++;
			if (!less(k, j)) break;
			exch(k, j);
			k = j;
		}
	}

	private boolean less(int i, int j) {
		return pq[i].compareTo(pq[j])<0;
	}

	private void exch(int i, int j) {
		Key swap = pq[i];
		pq[i] = pq[j];
		pq[j] = swap;
	}
}