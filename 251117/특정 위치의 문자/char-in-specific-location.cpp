#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    string input_chr;
    cin >> input_chr;

    vector<string> chr_lst = {"L", "E", "B", "R", "O", "S"};

    bool found = false;
    int idx = 0;

    for(int i = 0; i < chr_lst.size(); i++)
    {
        if(chr_lst[i] == input_chr)
        {
            idx = i;
            found = true;
            break;
        }
    }

    if(found)
        cout << idx << endl;
    else
        cout << "None" << endl;
    return 0;
}