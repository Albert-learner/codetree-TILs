#include <iostream>
#include <cmath>
using namespace std;

int n;
int arr[50];

int main() 
{
    cin >> n;

    for (int i = 0; i < n; i++) 
    {
        cin >> arr[i];
    }

    // Please write your code here.
    for(int i = 0; i < n; i++)
    {
        
        cout << (int)abs(arr[i]) << ' ';
    }

    return 0;
}