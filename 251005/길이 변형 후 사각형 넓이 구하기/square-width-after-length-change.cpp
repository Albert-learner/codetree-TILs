#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int width, length;
    cin >> width;
    cin >> length;

    width += 8;
    length *= 3;

    cout << width << endl;
    cout << length << endl;
    cout << width * length;
    return 0;
}