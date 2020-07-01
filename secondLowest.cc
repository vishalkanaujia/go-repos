#include<bits/stdc++.h>

using namespace std;

void print2Smallest(int arr[], int arr_size) 
{
    int second, first;
    if (arr_size < 2) {
        cout << "Invalid input" << endl;
        return;
    }

    second = first = INT_MAX;

    for (int i = 0; i < arr_size; i++) {
        if (arr[i] < first) {
            second = first;
            first = arr[i];
        }

        if (arr[i] < second && arr[i] > first) {
            second = arr[i];
        }
    }

    if (second == INT_MAX) {
        cout << "No second lowest" << endl;
        return;
    }

    cout << "Answer=" << second << endl;
}

/* Driver code */
int main()  
{  
    int arr[] = {12, 13, 1, 10, 34, 1};  
    int n = sizeof(arr)/sizeof(arr[0]);  
    print2Smallest(arr, n);  
    return 0;  
}  