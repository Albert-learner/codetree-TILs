#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N, M;
    cin >> N >> M;

    vector<long long> robotA, robotB;
    robotA.push_back(0);
    robotB.push_back(0);

    long long curA = 0, curB = 0;

    for (int i = 0; i < N; i++) 
    {
        long long size;
        char dir;
        cin >> size >> dir;

        if (dir == 'R') 
        {
            for (long long x = curA + 1; x <= curA + size; x++) robotA.push_back(x);
            curA += size;
        } 
        else 
        {
            for (long long x = curA - 1; x >= curA - size; x--) robotA.push_back(x);
            curA -= size;
        }
    }

    for (int i = 0; i < M; i++) 
    {
        long long size;
        char dir;
        cin >> size >> dir;

        if (dir == 'R') 
        {
            for (long long x = curB + 1; x <= curB + size; x++) robotB.push_back(x);
            curB += size;
        } 
        else 
        {
            for (long long x = curB - 1; x >= curB - size; x--) robotB.push_back(x);
            curB -= size;
        }
    }

    if (robotA.size() > robotB.size()) 
    {
        size_t diff = robotA.size() - robotB.size();
        robotB.insert(robotB.end(), diff, robotB.back());
    } 
    else if (robotB.size() > robotA.size()) 
    {
        size_t diff = robotB.size() - robotA.size();
        robotA.insert(robotA.end(), diff, robotA.back());
    }

    long long answer = 0;
    for (size_t i = 1; i < robotA.size(); i++) 
    {
        if (robotA[i] == robotB[i] && robotA[i - 1] != robotB[i - 1]) 
        {
            answer++;
        }
    }

    cout << answer << "\n";
    return 0;
}