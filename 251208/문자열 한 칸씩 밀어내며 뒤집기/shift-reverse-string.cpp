#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string input_str;
int q;

int main() 
{
    cin >> input_str >> q;

    for (int i = 0; i < q; i++) 
    {
        int query_type;
        cin >> query_type;
        if(query_type == 1)
        {
            char first = input_str[0];
            input_str.erase(input_str.begin());
            input_str.push_back(first);
        }
        else if(query_type == 2)
        {
            char last = input_str.back();
            input_str.pop_back();
            input_str.insert(input_str.begin(), last);
        }
        else if(query_type == 3)
            reverse(input_str.begin(), input_str.end());

        cout << input_str << endl;
    }
    return 0;
}
