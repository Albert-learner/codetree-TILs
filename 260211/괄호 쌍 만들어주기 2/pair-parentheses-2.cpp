#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string A;
    cin >> A;

    // Please write your code here.
    int N = A.length();
    int cnts = 0, result = 0;
    for(int i = N - 1; i > 0; i--)
    {
        if(A[i] == ')' && A[i - 1] == ')')
            cnts += 1;
        else if(A[i] == '(' and A[i - 1] == '(')
            result += cnts;
    }

    cout << result;
    return 0;
}