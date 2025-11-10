#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, a, b, even_sum = 0;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> a >> b;
        for(int i = a; i <= b; i++)
        {
            if(i % 2 == 0)
                even_sum += i;
        }
        cout << even_sum << endl;
        even_sum = 0;
    }
    
    return 0;
}