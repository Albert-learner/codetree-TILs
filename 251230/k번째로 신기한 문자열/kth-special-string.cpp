#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() 
{
    int N, K;
    string T;
    cin >> N >> K >> T;

    vector<string> words(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> words[i];
    }

    vector<string> satisfies;
    for (const string& word : words) 
    {
        if (word.compare(0, T.size(), T) == 0) {
            satisfies.push_back(word);
        }
    }

    sort(satisfies.begin(), satisfies.end());

    cout << satisfies[K - 1];
    return 0;
}
