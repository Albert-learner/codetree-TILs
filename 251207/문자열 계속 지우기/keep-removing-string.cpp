#include <iostream>
#include <string>
using namespace std;

string A, B;

int main() 
{
    cin >> A;
    cin >> B;
    
    // Please write your code here.
    int b_len = B.length();
    while(true)
    {
        size_t pos = A.find(B);
        if(pos == string::npos) break;
        A.erase(pos, b_len);
    }    
    cout << A;
    return 0;
}
