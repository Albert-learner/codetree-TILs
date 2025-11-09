#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    char cur_chr = 'A';
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        for(int s = 0; s < 2 * i; s++)
            cout << ' ';

        for(int j = 0; j < n - i; j++)
        {
            cout << cur_chr << ' ';
            cur_chr += 1;
            if(cur_chr > 'Z')
                cur_chr = 'A';
        }
        cout << endl;
    }
    return 0;
}