#include<bits/stdc++.h>

using namespace std;

float medianOfArray(int arr[], int size) 
{ 
  if (size % 2 == 0) // if size of array is even
    return (arr[size/2] + arr[size/2 - 1])/2.0; 
  else // size is odd
    return arr[size/2]; 
} 

float median(int arr1[], int arr2[], int size)
{
  // if there is only one element in each array,
  // then median is average of both elements
  if (size == 1) 
  {
    return (arr1[0] + arr2[0])/2.0;
  }
  // if each array has 2 elements then use this formula:
  else if (size == 2)
  {
    return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1]))/2.0;
  }
  else
  {
    float m1 = medianOfArray(arr1,size);
    float m2 = medianOfArray(arr2,size);

    // if the medians are equal, then the median
    // of both of them will also remain the same
    if (m1 == m2)
    {
      return m1;
    }
    // this is implementation of the algorithm described
    // in the illustration above
    if (m2 > m1)
    {
      // checking for even and odd number of elements
      // to make sure we get the array pointer
      // to the correct position of the median
      if (size % 2 == 0) 
      {
        return median(arr1 + size/2 - 1, arr2, size - size/2 + 1);
      }
      else
      {
        return median(arr1 + size/2, arr2, size - size/2); 
      } 
    }
    else if (m1 > m2)
    {
      if (size % 2 == 0) 
      {
	    	return median(arr1, arr2 + size/2 - 1, size - size/2 + 1); 
      }
      else
      {
	      return median(arr1, arr2 + size/2, size - size/2); 
      }
    }
  }
}

// driver code
int main()
{
  int arr1[] = {1,3,5};
  int arr2[] = {2,4,6};
  int size = sizeof(arr1)/sizeof(arr1[0]);
  float medianOfTwoArr = median(arr1, arr2, size);
  cout << "Median of the two arrays is: " << medianOfTwoArr;
  return 0;
}

https://www.educative.io/edpresso/how-to-find-the-median-of-two-sorted-arrays-in-cpp?https://www.educative.io/courses/grokking-the-object-oriented-design-interview?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=blog-dynamic