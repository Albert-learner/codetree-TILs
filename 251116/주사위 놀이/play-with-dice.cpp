#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int dice_num;
    vector<int> dice_cnts(6);

    for(int i = 0; i < 10; i++)
    {
        cin >> dice_num;
        dice_cnts[dice_num - 1] += 1;
    }

    for(int i = 0; i < dice_cnts.size(); i++)
        cout << i + 1 << " - " << dice_cnts[i] << endl;
    return 0;
}