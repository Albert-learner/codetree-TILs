#include <iostream>
#include <cmath>
using namespace std;

int st, ed;

int factors(int num)
{
    int elems = 0;

    for(int i = 1; i <= sqrt(num); i++)
    {
        if(num % i == 0)
        {
            elems += 1;
            if(i != num / i)
                elems += 1;
        }   
    }
    return elems;
}

int main() {
    cin >> st >> ed;

    // Please write your code here.
    int threes = 0;
    for(int i = st; i <= ed; i++)
    {
        if(factors(i) == 3)
            threes += 1;
    }
    cout << threes;
    return 0;
}
