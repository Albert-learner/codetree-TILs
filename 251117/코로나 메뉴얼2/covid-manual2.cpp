#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int arr_cnts[4] = {0, 0, 0, 0};
    int temps[3] = {0, 0, 0};
    string symptoms[3];

    for(int i = 0; i < 3; i++)
    {
        cin >> symptoms[i] >> temps[i];
    }

    for(int i = 0; i < 3; i++)
    {
        if(symptoms[i] == "Y" && temps[i] >= 37)
            arr_cnts[0] += 1;
        else if(symptoms[i] == "N" && temps[i] >= 37)
            arr_cnts[1] += 1;
        else if(symptoms[i] == "Y" && temps[i] < 37)
            arr_cnts[2] += 1;
        else if(symptoms[i] == "N" && temps[i] < 37)
            arr_cnts[3] += 1;
    }

    for(int i = 0; i < 4; i++)
        cout << arr_cnts[i] << ' ';

    if(arr_cnts[0] >= 2)
        cout << 'E';
    cout << endl;
    return 0;
}