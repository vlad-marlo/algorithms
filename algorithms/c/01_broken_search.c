#include <stdio.h>

int binary_search(int list[], int item, int len)
{
    int start = 0;
    int end = len;
    while (start <= len)
    {
        int mid = (start + end) / 2;
        int choice = list[mid];
        if (choice == item)
        {
            return mid;
        }
        if (choice > item)
        {
            end = mid - 1;
        }
        else 
        {
            start = mid + 1;
        }
    }
    return -1;
}

int main()
{
    int myList[] = {1, 2, 3, 4, 5, 6, 7};
    int len = sizeof(myList) / sizeof(myList[0]);
    int item = 2;
    int indexOfTwo = binary_search(myList, item, len);
    printf("item: %d at index: %d\n", item, indexOfTwo);
    return 0;
}
