#include <bits/stdc++.h>
#include <algorithm>    // std::swap

using namespace std;

int partition(int arr[], int low, int high);

void qsort(int arr[], int start, int end)
{
    int p;
    if (start < end)
    {
        p = partition(arr, start, end);
        qsort(arr, start, p - 1);
        qsort(arr, p + 1, end);
    }
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[low];
    int i = low;
    int j = high + 1;

    do {
        do {
            i++;
        } while (arr[i] < pivot && i <= high);

        do {
            j--;
        } while(arr[j] > pivot);

        if (i < j)
            swap(arr[i], arr[j]);

    } while (i < j);
    swap(arr[low], arr[j]);
    return j;
}

int main()
{
    int arr[] = {11,2,100,1,2,31};

    size_t size = sizeof(arr)/sizeof(arr[0]);
    qsort(arr, 0, size - 1);

    for (int i = 0; i < size; i++)
        cout << arr[i] << endl;
}