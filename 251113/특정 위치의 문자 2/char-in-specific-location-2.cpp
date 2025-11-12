#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<char> word(10);

    for(int i = 0; i < 10; i++)
    {
        cin >> word[i];
    }

    cout << word[1] << ' ' << word[4] << ' ' << word[7];
    return 0;
}