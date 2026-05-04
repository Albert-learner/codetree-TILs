#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int A, B, x, y;
    cin >> A >> B >> x >> y;

    // Please write your code here.
    if(A > B)
        swap(A, B);
    
    if (x > y)
        swap(x, y);

    vector<int> cases;
    if(A == x && B == y)
        cases.push_back(0);

    vector<int>line(101);
    int first_case = 0, second_case = 0, third_case = 0;

    line[A] = 1;
    line[B] = 2;

    first_case = abs(B - A);
    cases.push_back(first_case);

    second_case = abs(A - x) + abs(B - y);
    cases.push_back(second_case);

    third_case = abs(A - y) + abs(B - x);
    cases.push_back(third_case);

    cout << *min_element(cases.begin(), cases.end());

    return 0;
}
