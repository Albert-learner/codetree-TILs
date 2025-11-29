#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int a_cnts = 0, N, total_len = 0;
    cin >> N;
    vector<string>words(N);

    for(int i = 0; i < N; i++)
    {
        cin >> words[i];
        for(int j = 0; j < words[i].length(); j++)
        {
            if(words[i][j] == 'a')
                a_cnts += 1;
        }
        total_len += words[i].length();
    }

    cout << total_len << ' ' << a_cnts;
    return 0;
}