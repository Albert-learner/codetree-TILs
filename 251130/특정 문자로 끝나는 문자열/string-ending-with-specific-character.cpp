#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
    vector<string> words(10);
    string find_chr;

    for (int i = 0; i < 10; i++) 
    {
        cin >> words[i];
    }

    cin >> find_chr;

    vector<string> answer;

    for (const string& word : words) 
    {
        if (word.size() >= find_chr.size() &&
            word.substr(word.size() - find_chr.size()) == find_chr) 
        {
            answer.push_back(word);
        }
    }

    if (answer.empty()) 
    {
        cout << "None";
    } 
    else 
    {
        for (const string& w : answer) 
        {
            cout << w << "\n";
        }
    }

    return 0;
}
