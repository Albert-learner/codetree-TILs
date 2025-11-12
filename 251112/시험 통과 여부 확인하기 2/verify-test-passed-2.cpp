#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, finals = 0;
    double avg;
    cin >> n;
    vector<int> scores(4);

    for(int i = 0; i < n; i++)
    {
        cin >> scores[0] >> scores[1] >> scores[2] >> scores[3];
        avg = (scores[0] + scores[1] + scores[2] + scores[3]) / 4;
        if(avg >= 60)
        {
            cout << "pass" << endl;
            finals += 1;
        }
        else
            cout << "fail" << endl;
    }
    cout << finals;
    return 0;
}