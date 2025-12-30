#include <iostream>
#include <queue>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    priority_queue<int> left; 
    priority_queue<int, vector<int>, greater<int>> right; 

    for (int i = 1; i <= N; i++) 
    {
        int x;
        cin >> x;

        if (left.empty() || x <= left.top())
            left.push(x);
        else
            right.push(x);

        if (left.size() > right.size() + 1) 
        {
            right.push(left.top());
            left.pop();
        } 
        else if (right.size() > left.size()) 
        {
            left.push(right.top());
            right.pop();
        }

        // 인덱스가 홀수일 때 중앙값 출력
        if (i % 2 == 1) 
        {
            cout << left.top() << ' ';
        }
    }

    return 0;
}
