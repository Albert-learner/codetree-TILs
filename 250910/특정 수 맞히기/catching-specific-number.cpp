#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int score;
    cin >> score;

    while(score != 25)
    {
        if(score < 25)
            cout << "Higher" << endl;
        else
            cout << "Lower" << endl;

        cin >> score;
    }

    cout << "Good";
    return 0;
}