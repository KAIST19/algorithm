import java.lang.*;
import java.util.*;

public class quickSort {
	public static void main(String[] args) {
		int n;
		int[] arr;
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		Quick.sort(arr);

		for (int i = 0; i < n; i++) {
			System.out.println(arr[i]);
		}
	}
}

class Quick {
	public static void sort(int[] a) {
		sort(a, 0, a.length - 1);
	}

	public static void sort(int[] a, int lo, int hi) {
		if (hi <= lo) return;
		int j = partition(a, lo, hi);
		sort(a, lo, j - 1);
		sort(a, j + 1, hi);
	}

	private static int partition(int[] a, int lo, int hi) {
		int i = lo;
		int j = hi + 1;
		int v = a[lo];
		while (true) {
			while (a[++i] < v) {
				if (i == hi)
					break;
			}
			while (a[--j] > v) {
				if (j == lo)
					break;
			}
			if (i >= j) break;

			int temp;
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
		}
		int temp;
		temp = a[lo];
		a[lo] = a[j];
		a[j] = temp;
		return j;
	}
}