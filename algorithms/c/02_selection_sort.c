#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
#define SIZE 10

int get_min(int *list)
{
    int smallest = list[0];
    int smallest_idx = 0;
    for (int i = 1; i < SIZE; ++i)
    {
        if (list[i] < smallest)
        {
            smallest_idx = i;
            smallest = list[i];
        }
    }
    return smallest_idx;
}

int *selectionSort(int *array)
{
    int *newArr = (int *)malloc(SIZE * sizeof(int));
    for (int i = 0; i < SIZE; ++i)
    {
        int minI = get_min(array);
        newArr[i] = array[minI];
        array[minI] = INT_MAX;
    }
    return newArr;
}

int main()
{
    int arr [SIZE] = {9, 2, 1, 9, 2, 123, 0, -123, 23, 22};
    int *sorted = selectionSort(arr);
    for (int i = 0; i != SIZE; ++i)
    {
        printf("%d\n", sorted[i]);
    }
    return 0;
}
