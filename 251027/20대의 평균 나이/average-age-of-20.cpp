#include <iostream>
#include <vector>
#include <numeric>
#include <iomanip>
using namespace std;

int main() 
{
    int age;
    vector<int> ages;

    while (true) {
        cin >> age;
        if (age < 20 || age >= 30)
            break;
        ages.push_back(age);
    }

    if (ages.empty()) 
    {
        cout << "0.00";  
        return 0;
    }

    double ages_sum = accumulate(ages.begin(), ages.end(), 0);
    double avg = ages_sum / ages.size();

    cout << fixed << setprecision(2) << avg;
    return 0;
}
