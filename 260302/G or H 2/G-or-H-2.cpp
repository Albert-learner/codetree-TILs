#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N;
    cin >> N;

    vector<pair<int, char>> people;
    people.reserve(N);

    for (int i = 0; i < N; i++) 
    {
        int pos;
        string alpha;
        cin >> pos >> alpha;
        people.push_back({pos, alpha[0]});
    }

    // Please write your code here.
     vector<char> line(101, 0);
    for (auto &p : people) 
    {
        line[p.first] = p.second; // 'G' or 'H'
    }

    int answer = 0;
    for (int i = 0; i < (int)line.size(); i++) 
    {
        for (int j = i + 1; j < (int)line.size(); j++) 
        {
            if (line[i] == 0 || line[j] == 0) continue;

            int cnt_g = 0, cnt_h = 0;
            for (int k = i; k <= j; k++) 
            {
                if (line[k] == 'G') cnt_g++;
                else if (line[k] == 'H') cnt_h++;
            }

            if (cnt_g == 0 || cnt_h == 0 || cnt_g == cnt_h) 
            {
                int length = j - i;
                answer = max(answer, length);
            }
        }
    }

    cout << answer << "\n";
    return 0;
}