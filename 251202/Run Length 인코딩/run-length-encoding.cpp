#include <iostream>
#include <string>
#include <vector>
using namespace std;

string run_length_encoding(const string& input_str) 
{
    string ret_str;

    int n = input_str.length();
    if (n == 0) return ret_str; 

    vector<int> indices;
    indices.push_back(-1);

    for (int i = 0; i < n - 1; i++) 
    {
        if (input_str[i] != input_str[i + 1]) 
        {
            indices.push_back(i);
        }
    }
    indices.push_back(n - 1);

    vector<int> cnts_lst;
    for (int i = 0; i < (int)indices.size() - 1; i++) 
    {
        int diff = indices[i + 1] - indices[i];
        cnts_lst.push_back(diff);

    for (int i = 0; i < (int)cnts_lst.size(); i++) 
    {
        int chr_idx = indices[i + 1];
        int cnts = cnts_lst[i];
        ret_str += input_str[chr_idx];
        ret_str += to_string(cnts);
    }

    return ret_str;
}

int main() {
    string input_str;
    getline(cin, input_str);  // 공백 포함 문자열 입력

    string answer = run_length_encoding(input_str);
    cout << answer.length() << "\n";
    cout << answer << "\n";

    return 0;
}
