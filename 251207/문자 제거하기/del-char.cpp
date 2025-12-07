#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
    string input_str;
    cin >> input_str;

    vector<char> input_str_lst(input_str.begin(), input_str.end());

    while (input_str_lst.size() > 1) 
    {
        int idx;
        cin >> idx;

        if (idx >= input_str_lst.size()) 
        {
            input_str_lst.pop_back();
        } 
        else 
        {
            input_str_lst.erase(input_str_lst.begin() + idx);
        }

        // 출력
        for (char c : input_str_lst) 
        {
            cout << c;
        }
        cout << "\n";
    }
    return 0;
}
