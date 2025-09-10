#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    char f_chr;
    cin >> f_chr;
    
    vector<string> fives = {"apple", "banana", "grape", "blueberry", "orange"};
    vector<string> ans_lst;
    int answers = 0;

    for(const auto& word : fives)
    {
        if(word[2] == f_chr || word[3] == f_chr)
        {
            ans_lst.push_back(word);
            answers++;
        }
    }

    for(const auto& ans : ans_lst)
    {
        cout << ans << endl;
    }

    cout << answers << endl;
    return 0;
}