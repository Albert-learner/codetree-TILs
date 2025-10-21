#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int arr[5], num, evens = 0;

    for(int i = 0; i < 5; i++)
    {
        cin >> num;
        arr[i] = num;
    }

    for(int i = 0; i < 5; i++)
    {
        if(arr[i] % 2 == 0)
            evens += 1;
    }
    cout << evens;
    return 0;
}