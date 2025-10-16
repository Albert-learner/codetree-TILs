#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, c, num_lst[3] = {0};
    cin >> a >> b >> c;

    num_lst[0] = a;
    num_lst[1] = b;
    num_lst[2] = c;
    sort(num_lst, num_lst + 3);
    cout << num_lst[1];
    return 0;
}