#include <stdio.h>
#include <stdlib.h>

void quickSort(short *arr, int lo, int hi);
int partition(short *arr, int lo, int hi);

int main() {
    int n;
    short *arr;
    
    // declare an array with size of n
    scanf("%d", &n);
    arr = (short *)malloc(sizeof(short) * n);
    
    for(int i = 0; i < n; i++) {
        scanf("%hi", &arr[i]);
    }
    
    quickSort(arr, 0, n - 1);
    
    for(int i = 0; i < n; i++)
        printf("%hi\n", arr[i]);
    
    free(arr);
}

//quick sort
void quickSort(short *arr, int lo, int hi) {
    int j;
    
    if (lo >= hi) return;
    
    j = partition(arr, lo, hi);
    quickSort(arr, lo, j - 1);
    quickSort(arr, j + 1, hi);
}

int partition(short *arr, int lo, int hi) {
    int i = lo;
    int j = hi + 1;
    short v = arr[lo];
    
    while(1) {
        while (arr[++i] < v) {
            if (i == hi) break;
        }
        while (arr[--j] > v) {
            if (j == lo) break;
        }
        if (i >= j) break;
        
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    short temp = arr[lo];
    arr[lo] = arr[j];
    arr[j] = temp;
    
    return j;
}
