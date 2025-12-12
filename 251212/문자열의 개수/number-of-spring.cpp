#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() 
{
    int cnts = 0;
    vector<string> odds_lst;
    string input_str;

    while (true) 
    {
        getline(cin, input_str);

        if (input_str == "0") 
        {
            cout << cnts << endl;
            break;
        }

        cnts++;
        if (cnts % 2 == 1) 
        {
            odds_lst.push_back(input_str);
        }
    }

    for (const string& s : odds_lst) 
    {
        cout << s << endl;
    }

    return 0;
}
