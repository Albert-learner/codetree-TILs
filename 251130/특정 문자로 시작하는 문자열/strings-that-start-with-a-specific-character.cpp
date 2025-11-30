#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<string> words(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> words[i];
    }

    string find_chr;
    cin >> find_chr;

    int cnts = 0;
    int total_len = 0;

    for (const string& word : words) 
    {
        if (word.size() >= find_chr.size() && word.substr(0, find_chr.size()) == find_chr) 
        {
            cnts++;
            total_len += word.length();
        }
    }

    double avg_len = (cnts == 0) ? 0.0 : (double)total_len / cnts;

    cout << cnts << " " << fixed << setprecision(2) << avg_len;
    return 0;
}
