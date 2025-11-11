#include <iostream>
#include <vector>
#include <iomanip>
#include <numeric>
using namespace std;

int main() 
{
    // Please write your code here.
    double scores_sum = 0.0, avg;

    vector<double> scores(8);
    for(int i = 0; i < 8; i++)
    {
        cin >> scores[i];
    }
    scores_sum = accumulate(scores.begin(), scores.end(), 0.0);
    avg = scores_sum / 8;

    cout << fixed << setprecision(1) << avg;
    return 0;
}