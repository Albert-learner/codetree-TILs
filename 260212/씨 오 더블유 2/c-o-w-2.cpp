#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int n;
    string str;
    cin >> n;
    cin >> str;

    // Please write your code here.
    int answer = 0;
    for(int i = 0; i < n; i++)
    {
        for(int j = i + 1; j < n; j++)
        {
            for(int k = j + 1; k < n; k++)
            {
                if(str[i] == 'C' && str[j] == 'O' && str[k] == 'W')
                    answer += 1;
            }
        }
    }

    cout << answer;
    return 0;
}