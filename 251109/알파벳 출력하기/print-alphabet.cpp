#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    char cur_chr = 'A';
    cin >> n;

    for(int i = 1; i < n + 1; i++)
    {
        for(int j = 0; j < i; j++)
        {
            cout << cur_chr;
            cur_chr += 1;
            if(cur_chr > 'Z')
                cur_chr = 'A';
        }
        cout << endl;
    }
    return 0;
}