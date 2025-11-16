#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> scores;
    int x;

    while (cin >> x) 
    {
        if (x == 0) break;
        scores.push_back(x);
    }

    vector<int> n_scores;
    for (int score : scores) 
    {
        n_scores.push_back((score / 10) * 10);
    }

    vector<int> scores_cntr(11, 0);  
    for (int ns : n_scores)
    {
        if (ns >= 10 && ns <= 100) 
        {
            scores_cntr[ns / 10]++;  
        }
    }

    for (int v = 100; v >= 10; v -= 10) 
    {
        cout << v << " - " << scores_cntr[v / 10] << '\n';
    }

    return 0;
}
