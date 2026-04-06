#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int X, cur_pos = 0, cur_speed = 1, total_times = 0;
    cin >> X;
    
    // Please write your code here.
    while(true)
    {
        cur_pos += cur_speed;
        total_times += 1;
        cur_speed += 1;
        int gradients = 0;

        if(cur_pos == X)
            break;

        for(int i = 0; i < cur_speed; i++)
            gradients += i;

        if(X - (cur_pos + cur_speed) < gradients)
            cur_speed -= 1;

        int stays = 0;
        for(int i = 0; i < cur_speed; i++)
            stays += i;

        if(X - (cur_pos + cur_speed) < stays)
            cur_speed -= 1;

    }

    cout << total_times;
    return 0;
}