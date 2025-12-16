#include <iostream>
using namespace std;

int a, b;
int count_onjeonsus(int a, int b);

int main() 
{
    cin >> a >> b;

    // Please write your code here.
    cout << count_onjeonsus(a, b);
    return 0;
}

int count_onjeonsus(int a, int b)
{
    int cnts = 0;

    for (int num = a; num <= b; num++) 
    {
        if (num % 2 == 0) 
            continue;

        if (num % 10 == 5) 
            continue;

        if (num % 3 == 0 && num % 9 != 0) 
            continue;

        cnts += 1;
    }

    return cnts;
}