#include <iostream>
#include <vector>
#include <iomanip>
#include <numeric>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;
    double scores_sum = 0.0, avg;
    vector<double> scores(n);

    for(int i = 0; i < n; i++)
    {
        cin >> scores[i];
    }

    scores_sum += accumulate(scores.begin(), scores.end(), 0.0);
    avg = scores_sum / n;

    cout << fixed << setprecision(1) << avg << endl;
    if(avg >= 4.0)
        cout << "Perfect";
    else if(avg >= 3.0)
        cout << "Good";
    else
        cout << "Poor";
    return 0;
}