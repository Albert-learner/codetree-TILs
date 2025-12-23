#include <iostream>

using namespace std;

int n, m;
int A[100];
int operate(int M, int A_arr[]);

int main() 
{
    cin >> n >> m;

    for (int i = 0; i < n; i++) 
    {
        cin >> A[i];
    }

    // Please write your code here.
    cout << operate(m, A);
    return 0;
}

int operate(int M, int A_arr[])
{
    int answer = 0;

    while(M >= 1)
    {
        if(m % 2 == 1)
        {
            answer += A_arr[M - 1];
            M -= 1;
        }
        else
        {
            answer += A_arr[M - 1];
            M /= 2;
        }
    }

    return answer;
}