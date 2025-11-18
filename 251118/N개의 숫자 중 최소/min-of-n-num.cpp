#include <iostream>
#include <algorithm>
using namespace std;

int N, max_cst = 0, min_cst = 0, m_cnts = 0;
int A[100];

int main() 
{
    cin >> N;
    for (int i = 0; i < N; i++) 
    {
        cin >> A[i];
        max_cst = max(max_cst, A[i]);
    }

    // Please write your code here.
    min_cst = max_cst;
    for(int i = 0; i < N; i++)
    {
        min_cst = min(min_cst, A[i]);
    }

    for(int i = 0; i < N; i++)
    {
        if(A[i] == min_cst)
            m_cnts += 1;
    }
    cout << min_cst << ' ' << m_cnts;
    return 0;
}
