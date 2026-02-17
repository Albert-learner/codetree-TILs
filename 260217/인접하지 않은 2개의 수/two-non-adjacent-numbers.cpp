#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int n;
    int numbers[100];

    cin >> n;
    for (int i = 0; i < n; i++) 
    {
        cin >> numbers[i];
    }

    // Please write your code here.
    int two_sums = 0;
    for(int i = 0; i < n; i++)
    {
        for(int j = i + 2; j < n; j++)
        {
            if(numbers[i] + numbers[j] > two_sums)
                two_sums = numbers[i] + numbers[j];
        }
    }

    cout << two_sums;
    return 0;
}
